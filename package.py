import csv
from hashtable import ChainingHashTable


class Package:
    def __init__(self, id, address, deadline, city, state, zipcode, weight, status, special_instructions):
        self.ID = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.weight = weight
        self.status = status
        self.special_instructions = special_instructions

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.deadline, self.city, self.state, self.zipcode, self.weight, self.status)


def load_package(filename):
    package_dict = {} # initialize return value
    special_instructions_index = 7 #IDX where spec instructions live
    with open(filename) as packages:
        package_list = csv.reader(packages, delimiter=',')
        for package in package_list:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip_code = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_status = "Undelivered"
            special_instructions = False
            if special_instructions_index < len(package):
                special_instructions = True

            p = Package(package_id, package_address, package_deadline, package_city, package_state,
                        package_zip_code, package_weight, package_status, special_instructions)

            package_dict.update({package_id: p})
    return package_dict





