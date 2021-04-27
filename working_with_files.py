# Can remove FileNotFound for a general error
# errmsg generates error message in string form

def open_and_print_file(file="order.txt"):

    try:
        # default read mode
        with open(file, "x") as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print(f"There has been an error opening your file! \n{errmsg}")
        # Causes error again
    except FileExistsError:
        print(f"File \"{file}\" already exists!")
    finally:
        print("Execution complete")


def write_to_file(file="order.txt", order_item=""):
    try:
        with open(file, "a") as opened_file:
            opened_file.write(order_item + "\n")
    except FileNotFoundError:
        print("File can't be found!")


def write_multiple_lines_to_file(file="order.txt"):
    try:
        with open(file, "a") as opened_file:
            while True:
                order_item = input("Enter your item to input: ")
                opened_file.write(order_item + "\n")
                another_line = input("Another entry? (Y/N): ")
                if another_line == "N":
                    break

    except FileNotFoundError:
        print("File can't be found!")


# write_to_file("order.txt", "Lasagna")
# open_and_print_file("order.txt")
write_multiple_lines_to_file()