# a = tuple()
# b = (1, 2, 3)
# c = (2, 4, 1, 1)
#
# print(type(a))
# print(type(b))
# print(type(c))
#
# student_1 = {
#     "name": "Luke",
#     "stream": "data",
#     "list": {"value1": 1, "value2": 1, "value3": 2}
# }
#
# # print(student_1.keys())
# # print([x for x in student_1])
#
# # print(student_1.values())
# # print([student_1[x] for x in student_1])
#
# # print(student_1.items())
# # print([[x, y] for x, y in student_1.items()])
#
# print(student_1)
# print(student_1["list"]["value1"])

import random
import matplotlib.pyplot as plt
import csv

# min_num = 10
# max_num = 20
#
# a = [round(random.gauss(1/2 * (min_num + max_num), 1)) for i in range(0, 100)]
# print(a)

class SpartaSimulation:

    def __init__(self, months_to_simulate=12, centre_size=100, min_hired_trainees=20, max_hired_trainees=30):

        self.stopping_month = months_to_simulate + 1
        self.current_month = 1
        self.num_open_centres = 1
        self.num_full_centres = 0
        self.num_monthly_trainees = 0
        self.num_waiting_list = 0
        self.centers = {1: 0}
        self.centre_max_capacity = centre_size
        self.trainees_in_training = 0
        self.min_trainees = min_hired_trainees
        self.max_trainees = max_hired_trainees
        self.simulation_loop()

    def month_inc(self):
        self.current_month += 1

    def trainee_generator(self):
        self.num_monthly_trainees = random.randint(self.min_trainees, self.max_trainees)

    def get_num_open_centres(self):
        return self.num_open_centres

    def get_num_full_centres(self):
        return self.num_full_centres

    def get_num_current_trainees(self):
        return self.trainees_in_training

    def get_num_waiting_list(self):
        return self.num_waiting_list

    def add_new_center(self):
        new_center_id = len(self.centers.keys()) + 1
        self.num_open_centres += 1
        self.centers.update({new_center_id: 0})

    def plot_location_distributions(self):
        fig, ax = plt.subplots()
        ax.set_xlabel('Centre number')
        ax.set_ylabel('Trainees in centre')

        num_trainee_labels = []
        for i in sorted(self.centers.keys()):
            ax.bar(str(i), self.centers[i])
            num_trainee_labels.append(self.centers[i])
        ax.bar('waiting list', self.num_waiting_list, color='r')
        num_trainee_labels.append(self.num_waiting_list)
        for index, value in enumerate(num_trainee_labels):
            ax.text(index, (value + 2), str(value), ha='center', va='center')

        fig.savefig('filled_centres_bar.pdf')

    def csv_write(self, csv_file_name):
        with open(csv_file_name, 'w') as out_csv:
            fieldnames = ['trainee location', 'number of trainees']
            writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
            for i in sorted(self.centers.keys()):
                writer.writerow({'Centre '+str(i): self.centers[i]})
            writer.writerow({'waiting list': self.num_waiting_list})
        new_center_id = len(self.centers.keys()) + 1
        self.centers.update({new_center_id: 0})

    def assign_trainees_to_center(self):
        self.num_waiting_list += self.num_monthly_trainees
        for key in self.centers.keys():
            trainees = min(self.centre_max_capacity - self.centers[key], self.num_waiting_list)
            self.centers[key] += trainees
            self.trainees_in_training += trainees
            self.num_waiting_list -= trainees

    def simulation_loop(self):
        while self.current_month <= self.stopping_month:
            if self.current_month % 2 == 1 and self.current_month != 1:
                self.add_new_center()
            self.trainee_generator()
            self.assign_trainees_to_center()
            self.count_full_centers()
            self.month_inc()

    def count_full_centers(self):
        # Checks for each center if they're at max capacity yet.
        self.num_full_centres = sum(value == self.centre_max_capacity for value in self.centers.values())


SpartaSimulation_object = SpartaSimulation()
SpartaSimulation_object.simulation_loop()

print("Number of current trainees enrolled : " + str(SpartaSimulation_object.get_num_current_trainees()))

print("Number of open centres : " + str(SpartaSimulation_object.get_num_open_centres()))

print("Number of trainees in the waiting list : " + str(SpartaSimulation_object.get_num_waiting_list()))

print("Number of full centers : " + str(SpartaSimulation_object.get_num_full_centres()))


import pymongo
import requests
from pprint import pprint  # Remove later

def extract_from_api(url):
    """
    Will either, just return the data from a URL as a dictionary.
    Or specifically loop through the Star Wars API pages and extract the data into a list of dictionaries.
    """

    extract_list = []

    extract_status = requests.get(url).status_code

    # Gets data and converts to json
    data = requests.get(url).json()

    # Specifically checks for a key value, otherwise just return the data.
    if "results" in data.keys():
        extract_list += data["results"]
    else:
        return {"data": data, "status_code": extract_status}

    while data["next"]:
        # Link to next page is provided in the dict and converts to json
        data = requests.get(data["next"]).json()

        extract_list += data["results"]
    return {"data": extract_list, "status_code": extract_status}

# Extract starship data
starships_url = "https://swapi.dev/api/starships/"

starships_data = extract_from_api(starships_url)["data"]

pprint(extract_from_api(starships_url)["data"], sort_dicts=False)
print(len(extract_from_api(starships_url)["data"]))
print(extract_from_api(starships_url)["data"])

# client = pymongo.MongoClient()

# db.starships.drop()
