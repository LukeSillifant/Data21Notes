import json

pet_data = {"name": "bob", "food": "carrots"}

# print(pet_data)
# print(pet_data["food"])

# Serialises json format into a string (json is like a dictionary)
pet_data_json_string = json.dumps(pet_data)
# print(pet_data_json_string)

with open("new_json_file.json") as json_file:
    # json.dump(pet_data, json_file)
    pet = json.load(json_file)
    # print(type(pet))
    #     # print(pet["name"])


class RatesParser:

    def __init__(self, rates_json_file):
        rates_info = self._json_open_extract(rates_json_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        # self.gbp = rates_info["rates"]["GBP"]
        self.gbp = self.rates["GBP"]

    def _json_open_extract(self, file="exchange_rates.json"):
        with open(file) as rates:
            return json.load(rates)


rates_reader = RatesParser("exchange_rates.json")
print(rates_reader.gbp)
