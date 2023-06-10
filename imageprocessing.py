'''
2.0
https://open.kattis.com/problems/imageprocessing?tab=metadata
'''

image_height,image_width, kernel_height, kernel_width = map(int, input().split())

original_image = []
for _ in range(image_height):
    original_image.extend([int(i) for i in input().split()])

kernel = []
for _ in range(kernel_height):
    kernel.extend([int(i) for i in input().split()])


result_height = image_height - kernel_height + 1
result_width = image_width - kernel_width + 1

for result_height_i in range(result_height):
    result_row = []
    
    for result_width_i in range(result_width):
        entry = 0

        for kernel_height_i in range(kernel_height):
            for kernel_width_i in range(kernel_width):
                image_index = image_width * (result_height_i + kernel_height_i) + result_width_i + kernel_width_i

                kernel_index = kernel_width * (kernel_height - kernel_height_i - 1) + kernel_width - kernel_width_i - 1

                entry += original_image[image_index] * kernel[kernel_index]

        result_row.append(str(entry))

    print(' '.join(result_row))