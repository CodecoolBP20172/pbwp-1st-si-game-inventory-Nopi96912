import sys
import operator
import os
import csv

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'BuzogánԂ  ': 1}

def display_inventory(inventory):
    print("Inventory:")
    item_number = 0  # variable to count the items in the dictionary
    for k, v in inventory.items():
        print(str(v) + " " + str(k))  # prints the item with the item amount
        item_number += v  # adds the amount of value to the variable
    print("Total number of items: " + str(item_number))

# display_inventory(inv)

def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)  # watches if item in the list
        inventory[added_items[i]] = inventory[added_items[i]] + 1
    return inventory

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
# display_inventory(inv)

def print_table(inventory, order=None):
    coloum_size = int(max(len(x) for x in inventory))  # looks for the longest item in the inventory
    print('Inventory:' '\n'
          'count:'.rjust(coloum_size) + 'item name:'.rjust(coloum_size * 2))
    if order == 'count,desc':  # prints dictionary in a descanding order
        descending_inv = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
        for k, v in descending_inv:
            print(str(v).rjust(coloum_size) + k.rjust(coloum_size * 2))
        print('Total number of items:', sum(inventory.values()))
    elif order == 'count,asc':  # prints dictionary in a ascending order
        ascending_inv = sorted(inventory.items(), key=operator.itemgetter(1))
        for k, v in ascending_inv:
            print(str(v).rjust(coloum_size) + k.rjust(coloum_size *2))
        print('Total number of items:', sum(inventory.values()))
    else:  # Prints dictionary in a random order
        for k, v in inventory.items():
            print(str(v).rjust(coloum_size) + k.rjust(coloum_size *2))
        print('Total number of items:', sum(inventory.values()))
# print_table(inv)

def import_inventory(inventory, filename="import_inventory.csv"):
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile)
        imported_inventory = list(reader)  # make a list from the imported data
        add_to_inventory(inventory, imported_inventory[0])
        
import_inventory(inv, sys.argv[1])
# print_table(inv, 'count,desc')

def export_inventory(inventory, filename="export_inventory.csv"):
        bag = []  # a temporary list for the data to export
        writer = csv.writer(open(filename, 'w'), quoting=csv.QUOTE_NONE, escapechar="|")
        for key, value in inventory.items():
            for i in range(value):
                bag.append(key)
        writer.writerow(bag)

export_inventory(inv)