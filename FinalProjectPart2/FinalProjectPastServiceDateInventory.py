#Name: Juan Gonzalez
#ID: 1808943

import csv
from datetime import datetime

# Creates an empty list
items = {}
# This list holds the names of each file type
files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']

# Cycles through each file name, opening the related file
for file in files:
    with open(file, 'r') as read_file:
        file_reader = csv.reader(read_file, delimiter=',')
        # Goes through each line within the file
        for line in file_reader:
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
            # ManufacturerList.csv and store it as readable variables
            elif file == files[2]:
                service_date = line[1]
                items[item_id]['service_date'] = service_date

#Takes the dates from the excel document and converts them to a format that can
#compared to the current date
keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y"), reverse=True)
# This section opens the needed file to write to.
with open('PastServiceDateInventory.csv', 'w') as write_file:
    #Goes through each item in keys and assigns their attribute
    #to the approriate variable
    for item in keys:
        id = item
        man_name = items[item]['manufacturer']
        item_type = items[item]['item_type']
        price = items[item]['price']
        service_date = items[item]['service_date']
        damaged = items[item]['damaged']
        #Creates variables for todays date
        today = datetime.now()
        #Formats the expiration date in the corrects format to compare it to "today"
        service_expiration = datetime.strptime(service_date, "%m/%d/%Y")
        #Determenies if the expiration date occured before today
        expired = service_expiration < today
        #If the item is expired, it is added to the csv.
        if expired:
            file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

read_file.close()
write_file.close()
