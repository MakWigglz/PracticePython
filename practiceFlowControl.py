def print_list_elements():
    lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
    lst2 = [134, 'dcf', 23.77, ['h', 'fgt', 122.987], 'mak', 55]
    lst3 = ['i love sushi', 'i hate lying vets']

    print(lst3[0])
    print(lst2[4:6])
    print(lst3[1])
    
print_list_elements()    
    
import cv2
from turtle import *

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Threshold the image to binary
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_signature_from_image(image_path):
    contours = process_image(image_path)
    # Initialize turtle
    shape("turtle")
    speed(0)
    penup()
    
    for contour in contours:
        for point in contour:
            x, y = point[0]
            goto(x - 200, 200 - y)  # Adjust coordinates as needed
            pendown()
        penup()

# Example usage
draw_signature_from_image('path_to_signature_image.png')
done() 
