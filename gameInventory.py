import sys
import operator
import os
import csv
# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    item_number = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_number += v
    print("Total number of items: " + str(item_number))

# display_inventory(inv)

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] = inventory[added_items[i]] + 1
    return inventory

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
# display_inventory(inv)

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    coloum_size = int(max(len(x) for x in inventory))
    print('Inventory:' '\n'
          'count:'.rjust(coloum_size) + 'item name:'.rjust(coloum_size *2))
    if order == 'count,desc':
        descending_inv = sorted(inventory.items(), key = operator.itemgetter(1), reverse=True)
        for k, v in descending_inv:
            print(str(v).rjust(coloum_size) + k.rjust(coloum_size *2))
        print('Total number of items:', sum(inventory.values()))
    elif order == 'count,asc':
        ascending_inv = sorted(inventory.items(), key = operator.itemgetter(1))
        for k, v in ascending_inv:
            print(str(v).rjust(coloum_size) + k.rjust(coloum_size *2))
        print('Total number of items:', sum(inventory.values()))
    else:
        for k, v in inventory.items():
            print(str(v).rjust(coloum_size) + k.rjust(coloum_size *2))
        print('Total number of items:', sum(inventory.values()))
# print_table(inv)

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open (sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile)
        imported_inventory = list(reader)
        add_to_inventory(inventory, imported_inventory[0])
        # print(imported_inventory)

import_inventory(inv, sys.argv[1])
print_table(inv, 'count,desc')

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
        bag = []
        writer = csv.writer(open(filename, 'w'), quoting=csv.QUOTE_NONE, escapechar="|")
        for key, value in inventory.items():
            for i in range(value):  # we put the key (item) to the list [value] times
                bag.append(key)
        writer.writerow(bag)  # and finally we write it to the file
export_inventory(inv)