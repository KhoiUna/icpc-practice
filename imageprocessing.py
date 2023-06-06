'''
2.0
https://open.kattis.com/problems/imageprocessing?tab=metadata
'''

imageHeight,imageWidth,kernelHeight,kernelWidth = map(int, input().split())

matrix = []
for _ in range(imageHeight):
    matrix.extend([int(i) for i in input().split()])

kernel = []
for _ in range(kernelHeight):
    kernel.extend([int(i) for i in input().split()])

resultingImageHeight = imageHeight - kernelHeight + 1
resultingImageWidth = imageWidth - kernelWidth + 1

for resultingImageHeightIndex in range(resultingImageHeight):
    resultingImageRow = []
    for resultingImageWidthIndex in range(resultingImageWidth):
        entry = 0
        for kernelHeightIndex in range(kernelHeight):
            for kernelWidthIndex in range(kernelWidth):
                imageHeightIndex = imageWidth * (resultingImageHeightIndex + kernelHeightIndex)
                imageWidthIndex = resultingImageWidthIndex + kernelWidthIndex
                imageIndex = imageHeightIndex + imageWidthIndex
                imageValue = matrix[imageIndex]

                kernelIndex = kernelWidth * (kernelHeight - kernelHeightIndex - 1) + (kernelWidth - kernelWidthIndex - 1)
                kernelValue = kernel[kernelIndex]
                entry += imageValue * kernelValue
        resultingImageRow.append(str(entry))

    print(" ".join(resultingImageRow))