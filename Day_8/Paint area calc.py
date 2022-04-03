import math

def paint_calc(height, width, cover):
    area = height * width
    Number_Of_Cans = math.ceil(area / cover)
    print(f"You will need {Number_Of_Cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# def Number_Of_Cans(height, width):
#     coverage = 5
#     area = int(height) * int(width)
#     required = round(area / coverage)
#     print(required)

# Number_Of_Cans(5, 2)
