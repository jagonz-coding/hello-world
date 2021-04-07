#Name: Juan Gonzalez
#ID: 1808943

import csv

# Creates an empty list
items = {}
# This list holds the names of each file type
files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']

# Cycles through each file name, opening the related file
for file in files:
    with open(file, 'r') as read_file:
        file_reader = csv.reader(read_file, delimiter=',')
        # Goes through each line within thefile
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
            # ManufacturerList.csv and store it as readable varaibles
            elif file == files[2]:
                service_date = line[1]
                items[item_id]['service_date'] = service_date

# This section opens the needed file to write to.
with open('FullInventory.csv', 'w') as write_file:
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
        write_file.write('{},{},{},{},{},{}\n'.format(id, m_name, item_type, price, service_date, damaged))

read_file.close()
write_file.close()
