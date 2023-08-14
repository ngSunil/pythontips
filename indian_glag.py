def create_indian_flag():
    flag_height = 9
    flag_width = 13
    saffron = '\033[48;2;255;153;51m'
    white = '\033[48;2;255;255;255m'
    green = '\033[48;2;19;136;8m'
    navy_blue = '\033[48;2;0;56;168m'
    reset_color = '\033[m'

    flag = []

    # Calculate the vertical position of the Ashok Chakra
    chakra_vertical_position = flag_height // 2

    # Create the flag stripes
    for i in range(flag_height):
        if i < flag_height // 3:
            flag.append(saffron + " " * flag_width)
        elif i < 2 * (flag_height // 3):
            flag.append(white + " " * flag_width)
        else:
            flag.append(green + " " * flag_width)

    # Create the Ashok Chakra (Navy Blue Circle)
    chakra_center_x = flag_width // 2
    chakra_radius = flag_width // 6

    for i in range(flag_height):
        row = ""
        for j in range(flag_width):
            distance = ((i - chakra_vertical_position) **
                        2 + (j - chakra_center_x) ** 2) ** 0.5
            if distance <= chakra_radius:
                row += navy_blue + " " + reset_color
            else:
                row += " "
        flag.append(row)

    # Print the flag
    for line in flag:
        print(line)


if __name__ == "__main__":
    create_indian_flag()
