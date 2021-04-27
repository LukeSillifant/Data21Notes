import csv


def csv_open_extract(file="user_details.csv"):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_list = list(csv_reader)
        return csv_list

    # Prints fifth column
    # for row in csv_reader:
    #     print(row[4])

    # No headings
    # iterable_csv = iter(csv_reader)
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row)


# def transformation_user_details(file="user_details.csv"):
#     # Only saves names and email address
#     with open(file) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=",")
#         iterable_csv = iter(csv_reader)
#         next(iterable_csv)
#         for row in iterable_csv:
#             print(row[1], row[2], row[4])

# Only saves names and email address in a list of lists
def csv_transform_list(csv_list):

    csv_list = csv_list[1:]
    list_output = []
    for row in csv_list:
        list_output.append([row[i] for i in [1, 2, 4]])
    return list_output

# transformation_user_details()
# transformation_user_details_list()


def csv_create_file(csv_list, cvs_file="new_details.csv"):

    with open(cvs_file, 'w') as new_file:
        csv_writer = csv.writer(new_file, lineterminator='\n')
        csv_writer.writerows(csv_list)


csv_read = csv_open_extract()
csv_transformed = csv_transform_list(csv_read)
csv_create_file(csv_transformed)
