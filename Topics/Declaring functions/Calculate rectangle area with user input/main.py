# Import necessary libraries

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width


# Main program
def main():
    length = float(input())
    width = float(input())

    area = calculate_area(length, width)
    print(area)

if __name__ == "__main__":
    main()