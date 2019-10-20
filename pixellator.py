from PIL import Image
import os

print(os.getcwd())


original = Image.open(input("Filepath of image to pixellate: "))
originalPix = original.load()
pixFactor = int(input("Pixellation factor (2-50): "))

temp = (original.size[0] // pixFactor + original.size[0] % pixFactor, original.size[1] // pixFactor + original.size[1] % pixFactor)
pixellated = Image.new("RGB", original.size)
newPix = pixellated.load()

for x in range(original.size[0] // pixFactor):
    for y in range(original.size[1] // pixFactor):
        avR = 0
        for i in range(pixFactor):
            avR += originalPix[x * pixFactor + i, y * pixFactor][0]
            avR += originalPix[x * pixFactor, y * pixFactor + i][0]
            avR += originalPix[x * pixFactor + 1, y * pixFactor + i][0]
        avR //= pixFactor ** 2

        avG = 0
        for i in range(pixFactor):
            avG += originalPix[x * pixFactor + i, y * pixFactor][1]
            avG += originalPix[x * pixFactor, y * pixFactor + i][1]
            avG += originalPix[x * pixFactor + 1, y * pixFactor + i][1]
        avG //= pixFactor ** 2

        avB = 0
        for i in range(pixFactor):
            avB += originalPix[x * pixFactor + i, y * pixFactor][2]
            avB += originalPix[x * pixFactor, y * pixFactor + i][2]
            avB += originalPix[x * pixFactor + 1, y * pixFactor + i][2]
        avB //= pixFactor ** 2

        newPix[x, y] = (avR, avG, avB)

pixellated.show()
