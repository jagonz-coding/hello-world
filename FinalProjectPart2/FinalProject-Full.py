#Name: Juan Gonzalez
#ID: 1808943

import csv
from datetime import datetime

class OutputInventory:
    # Class for methods used to create output inventory files from provided input
    # Files created under the output_files directory. This directory is expected to be there
    def __init__(self, item_list):
    #Must provide list of all items to create new files
        self.item_list = item_list

    # This section opens the needed file to write to.
    def full(self):
        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            # Sorts the file in alphabetical order, based on the manufacturer name (m_name)
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                # After being sorted, the gathered information can now be assigned to their own variable
                id = item
                m_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                # The variables can now be printed onto the file in the list, seperated by spaces and commas
                file.write('{},{},{},{},{},{}\n'.format(id, m_name, item_type, price, service_date, damaged))

    def inv_type(self):
        items = self.item_list
        # Creates an empty list to store the different types of electronics
        types = []
        # Sorts out the items in the list
        keys = sorted(items.keys())
        # Goes through each item in the list until the last one is reached.
        for item in items:
            item_type = items[item]['item_type']
            # Adds a type to the list only if it has not been added
            if item_type not in types:
                types.append(item_type)
                # Assigns name to file_name if a new type is found
                for type in types:
                    file_name = type.capitalize() + 'Inventory.csv'
            # This section opens the needed file to write to.
            with open(file_name, 'w') as file:
                # Goes through each item in keys until the last one is reached
                for item in keys:
                    # The gathered information can now be assigned to their own variable
                    id = item
                    m_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    # If the type equal the current item_type, the variables can be printed out to the current file
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, m_name, price, service_date, damaged))

    def past_service(self):
        items = self.item_list
        # Takes the dates from the excel document and converts them to a format that can
        # compared to the current date
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y"), reverse=True)
        # This section opens the needed file to write to.
        with open('PastServiceDateInventory.csv', 'w') as file:
            # Goes through each item in keys and assigns their attribute
            # to the approriate variable
            for item in keys:
                id = item
                m_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                # Creates variables for todays date
                today = datetime.now()
                # Formats the expiration date in the corrects format to compare it to "today"
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y")
                # Determenies if the expiration date occured before today
                expired = service_expiration < today
                # If the item is expired, it is added to the csv.
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, m_name, item_type, price, service_date, damaged))

    def damaged(self):
        items = self.item_list
        # Sorts the the items in order from most expensive to least expensive
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        # Opens the DamagedInventory file to begin writing to it
        with open('DamagedInventory.csv', 'w') as file:
            # Goes through each item in keys and assigns their attribute
            # to the approriate variable
            for item in keys:
                id = item
                m_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                # If the damaged variable is assigned with "damaged",
                # the item and its' attributes is added to the csv
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, m_name, item_type, price, service_date))


if __name__ == '__main__':
    # Creates an empty list
    items = {}
    # This list holds the names of each file type
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    # Cycles through each file name, opening the related file
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Goes through each line within the file
            for line in csv_reader:
                item_id = line[0]
                # First "if" statement is meant to get information from the
                # ManufacturerList.csv and store it as readable varaibles
                if file == files[0]:
                    items[item_id] = {}
                    m_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    # I use the strip function to remove any spaces and clean up the
                    # the variables.
                    items[item_id]['manufacturer'] = m_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                # Second "if" statement is meant to get information from the
                # ServiceDatesList.csv and store it as readable variables
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                # Third "if" statement is meant to get information from the
                # ManufacturerList.csv and store it as readable varaibles
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    # Brings over "items" from the OutputInventory class and
    # applies it to the "inventory" variable in this section
    inventory = OutputInventory(items)
    # Output files are created
    inventory.full()
    inventory.inv_type()
    inventory.past_service()
    inventory.damaged()

    # Lists for both the "types" and "manufacturers" are created and have
    # their items added to them
    types = []
    manufacturers = []
    # Loop goes through every item in "items" and appends them to their
    # respective list if a match is found
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)

    # This section is where the user is asked for input
    # Depending on their response, the program may stop or continue
    user_input = None
    while user_input != 'q':
        user_input = input("\nPlease enter an item manufacturer and item type or enter 'q' to quit:\n")
        if user_input == 'q':
            break
        else:
            # Checks the users input to see if a match can be
            # found in the the "types" and "manufacturers" list
            selected_manufacturer = None
            selected_type = None
            user_input = user_input.split()
            bad_input = False
            for word in user_input:
                # Compares input to items in "manufacturers"
                # if a match is found, bad_input is set to true
                # If not, input is applied to "word"
                if word in manufacturers:
                    if selected_manufacturer:
                        bad_input = True
                    else:
                        selected_manufacturer = word
                # Compares input to items in "manufacturers"
                # if a match is found, bad_input is set to true
                # If not, input is applied to "word"
                elif word in types:
                    if selected_type:
                        bad_input = True
                    else:
                        selected_type = word
            if not selected_manufacturer or not selected_type or bad_input:
                print("No such item in inventory")
            else:
                # Keys is set as a sorted version of the
                # items list from highest to lowest price
                keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

                # List is created to store the matching items words
                matching_items = []
                # "similar_items" is basically "matching_items", but is meant to
                # to items with the same type, be in inventory (not damaged or past service),
                # and must have different manufacturers
                similar_items = {}
                for item in keys:
                    if items[item]['item_type'] == selected_type:
                        today = datetime.now()
                        service_date = items[item]['service_date']
                        service_expiration = datetime.strptime(service_date, "%m/%d/%Y")
                        expired = service_expiration < today
                        # Makes sure the item meets the requirements listed above to be added to
                        # added to the "matching_items"
                        if items[item]['manufacturer'] == selected_manufacturer:
                            if not expired and not items[item]['damaged']:
                                matching_items.append((item, items[item]))
                        # Makes sure the item meets the requirements listed above to be added to
                        # added to the "similar_items"
                        else:
                            if not expired and not items[item]['damaged']:
                                similar_items[item] = items[item]

                # Any matching items can now be output to the user here,
                # along with their ID, manufacturer name (m_name), type, and price
                if matching_items:
                    item = matching_items[0]
                    item_id = item[0]
                    m_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']
                    print("Your item is: {}, {}, {}, {}\n".format(item_id, m_name, item_type, price))

                    # If the item is not meet requirement for "matching_items", they can be output under
                    # similar items, going by which one it has a closer price to.
                    if similar_items:
                        matched_price = price
                        # This section finds the item with the closes price by comparing the
                        # disparity in their item price, choosing the smallest difference
                        closest_item = None
                        closest_price_diff = None
                        for item in similar_items:
                            if closest_price_diff is None:
                                closest_item = similar_items[item]
                                closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                m_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < closest_price_diff:
                                closest_item = item
                                closest_price_diff = price_diff
                                item_id = item
                                m_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, m_name, item_type, price))
                        else:
                            print("No such item in inventory\n")
