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

# Unit test

import unittest
from spartasim import SpartaSimulation


class SpartaSimulationTests(unittest.TestCase):

    def setUp(self):
        self.months_to_simulate = 10
        self.min_trainees = 20
        self.max_trainees = 30
        self.sim = SpartaSimulation(self.months_to_simulate, self.min_trainees, self.max_trainees)

    def test_month_inc(self):
        initial_value = self.sim.current_month
        self.sim.month_inc()
        self.assertIs(type(self.sim.current_month), int)
        self.assertEqual(self.sim.current_month, initial_value + 1)
        self.sim.current_month = initial_value

    def test_trainee_generator(self):
        random_number = self.sim.trainee_generator()
        self.assertIs(type(self.sim.current_month), int)
        self.assertGreaterEqual(random_number, self.sim.min_trainees)
        self.assertLessEqual(random_number, self.sim.max_trainees)

    def test_assign_trainee_to_course(self):
        self.sim.assign_trainee_to_course()
        self.assertEqual(sum(value != "None" for value in self.sim.trainee_df["Assigned centre ID"]), 0)
        self.assertEqual(sum(value not in self.sim.courses for value in self.sim.trainee_df["Course type"]), 0)
        self.assertEqual(sum(value != 0 for value in self.sim.trainee_df["Start month"]), 0)
        self.assertEqual(sum(value != 0 for value in self.sim.trainee_df["Stop month"]), 0)
        self.assertEqual(sum(value != "Waiting" for value in self.sim.trainee_df["Status"]), 0)

    def test_create_centre(self):

        self.sim.create_centre()

        self.assertEqual(
            sum(value not in self.sim.available_centre_types for value in self.sim.centres_df["Centre type"]), 0)
        self.assertEqual(sum(value != 0 for value in self.sim.centres_df["Trainee count"]), 0)
        self.assertEqual(sum(value != 0 for value in self.sim.centres_df["Low att month counter"]), 0)
        self.assertEqual(sum(value != "open" for value in self.sim.centres_df["Centre status"]), 0)

        for value in range(0, len(self.sim.centres_df)):
            if self.sim.centres_df["Centre type"][value] == "Hub":
                self.assertEqual(self.sim.centres_df["Max capacity"][value], 100)
                self.assertEqual(self.sim.centres_df["Centre course type"][value], "None")

            if self.sim.centres_df["Centre type"][value] == "Boot camp":
                self.assertEqual(self.sim.centres_df["Max capacity"][value], 500)
                self.assertEqual(self.sim.centres_df["Centre course type"][value], "None")

            if self.sim.centres_df["Centre type"][value] == "Tech centre":
                self.assertEqual(self.sim.centres_df["Max capacity"][value], 200)
                self.assertEqual(sum(value not in self.sim.available_tech_centre_types for value in
                                     self.sim.centres_df["Centre course type"]), 0)

    def test_count_centres(self):
        # Empty test
        self.sim.centres_df = self.sim.centres_df.iloc[0:0]
        self.sim.count_centres()
        self.assertEquals(self.sim.available_tech_centre_types, ['Java', 'C#', 'Data', 'DevOps', 'Business'])

        # Not empty test, all centres available
        self.sim.centres_df = self.sim.centres_df.iloc[0:0]
        self.sim.centres_df.append(["Hub", 0, 100, 0, "None", "open"], ignore_index=True)

    def test_complete_trainees(self):
        self.sim.current_month = 13

        self.sim.centres_df = self.sim.trainee_df.iloc[0:0]
        self.sim.trainee_df = self.sim.trainee_df.iloc[0:0]

        self.sim.centres_df.append([{'Centre type': "Hub", 'Trainee count': 1, 'Max capacity': 100,
                                     'Low att month counter': 0, 'Centre course type': "None",
                                     'Centre status': "open"}])
        self.sim.centres_df.append([{'Centre type': "Tech centre", 'Trainee count': 1, 'Max capacity': 200,
                                     'Low att month counter': 0, 'Centre course type': "Data",
                                     'Centre status': "open"}])

        self.sim.trainee_df.append([{"Assigned centre ID": 'Hub', "Course type": "Java", "Start month": 1,
                                     "Stop month": 13, "Status": "Training"}], ignore_index=True)
        self.sim.trainee_df.append([{"Assigned centre ID": "Tech centre", "Course type": "Data", "Start month": 5,
                                     "Stop month": 17, "Status": "Training"}], ignore_index=True)
        self.sim.complete_trainees()

        self.assertEqual(self.sim.trainee_df["Assigned centre ID"][0], "None")
        self.assertEqual(self.sim.trainee_df["Status"][0], "Benched")

        # self.assertEqual(self.sim.trainee_df["Assigned centre ID"][1], "Tech centre")
        # self.assertEqual(self.sim.trainee_df["Status"][1], "Training")

        # self.assertEqual(self.sim.centres_df["Trainee count"][0], 0)
        # self.assertEqual(self.sim.centres_df["Trainee count"][1], 1)

        # finish test

    # # tests get functions:
    # def test_get_num_open_centres(self):
    #     self.assertEqual(self.sim.get_num_open_centres(), 6)
    #
    # def test_get_num_full_centres(self):
    #     self.assertEqual(self.sim.get_num_full_centres(), 2)
    #
    #
    # def test_get_num_waiting_list(self):
    #     self.assertEqual(self.sim.get_num_waiting_list(), 0)
    #
    #
    # def test_assign_trainee_to_center(self):
    #     for v in self.sim.centers.values():
    #         self.assertLessEqual(v, 100)
    #
    #     self.sim.num_monthly_trainees = 0
    #
    #     self.sim.centers = {1: 50}
    #     self.sim.num_waiting_list = 150
    #     self.sim.assign_trainees_to_center()
    #     self.assertEqual(self.sim.centers[1], 100)
    #     self.assertEqual(self.sim.num_waiting_list, 100)
    #
    #     self.sim.centers = {1: 50}
    #     self.sim.num_waiting_list = 30
    #     self.sim.assign_trainees_to_center()
    #     self.assertEqual(self.sim.centers[1], 80)
    #     self.assertEqual(self.sim.num_waiting_list, 0)
    #
    #     self.sim.centers = {1: 100, 2: 50}
    #     self.sim.num_waiting_list = 20
    #     self.sim.assign_trainees_to_center()
    #     self.assertEqual(self.sim.centers[1], 100)
    #     self.assertEqual(self.sim.centers[2], 70)
    #     self.assertEqual(self.sim.num_waiting_list, 0)
    #
    #     self.sim.centers = {1: 0, 2: 0}
    #     self.sim.num_waiting_list = 150
    #     self.sim.assign_trainees_to_center()
    #     self.assertEqual(self.sim.centers[1], 100)
    #     self.assertEqual(self.sim.centers[2], 50)
    #     self.assertEqual(self.sim.num_waiting_list, 0)
    #
    #     self.sim.centers = {1: 100, 2: 90}
    #     self.sim.num_waiting_list = 20
    #     self.sim.assign_trainees_to_center()
    #     self.assertEqual(self.sim.centers[1], 100)
    #     self.assertEqual(self.sim.centers[2], 100)
    #     self.assertEqual(self.sim.num_waiting_list, 10)

    # def test_count_full_centers(self):
    #     self.sim.centers = {1: 100, 2: 100, 3: 50}
    #     self.sim.count_full_centers()
    #     self.assertEqual(self.sim.num_full_centres, 2)
    #
    #     self.sim.centers = {1: 0, 2: 0, 3: 50}
    #     self.sim.count_full_centers()
    #     self.assertEqual(self.sim.num_full_centres, 0)
    #
    #     self.sim.centers = {1: 100, 2: 100, 3: 100}
    #     self.sim.count_full_centers()
    #     self.assertEqual(self.sim.num_full_centres, 3)
    #
    #     self.sim.centers = {1: 100, 2: 100, 3: 50, 4: 30, 5: 100}
    #     self.sim.count_full_centers()
    #     self.assertEqual(self.sim.num_full_centres, 3)
