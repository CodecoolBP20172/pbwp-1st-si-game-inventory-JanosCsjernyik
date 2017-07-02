# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
import csv
import os


def display_inventory(inventory):
    summa = 0
    print("Inventory:")
    for keys, values in inventory.items():
        print(values, keys)
        summa += values
    print("Total number of items: %d" % summa)
    pass


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    #for newItem in range(len(added_items)):
    #    for items in list(inventory):
    #        if added_items[newItem] == items:
    #            inventory[items] += 1
    #        if added_items not in list(inventory):
    #            inventory[added_items[newItem]] = 1
    #return inventory
    for item in added_items:
        if item in inventory.keys():
            inventory[item] +=1
        else:
            inventory[item] = 1




# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    values = list(inventory.values())
    keys = list(inventory.keys())
    key_length = len(max(keys, key=len))
    value_length = len(str(max(values)))
    total = key_length + value_length
    inventory_asc = sorted(inventory.items(), key=operator.itemgetter(1))
    inventory_desc = reversed(inventory_asc)
    pairlist =[]
    for a, b in zip(keys, values):
        pairlist.extend([b, a])
    print(pairlist)
    
    summa = 0
    for key, value in inventory.items():
        summa += value
    print(value_length)    
    print("Inventory:\n")
    print("count"  +" " *(key_length - 9) + "item name")
    print("-" * total)
    if order == "count,asc":
        for item in inventory_asc:
            print(" "*(value_length - len(str(item[1]))), item[1],
                  " "*(key_length - len(str(item[0]))), item[0])

    elif order == "count,desc":
        for item in inventory_desc:
            print(" "*(value_length - len(str(item[1]))), item[1],
                  " "*(key_length - len(str(item[0]))), item[0])

    elif order == None:
        for item in pairlist:
            print(" "*(value_length - len(str(item[0]))), item[0],
                  " "*(key_length - len(str(item[1]))), item[1])
    else:
        raise ValueError("Invalid parameter for order")


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as read:
        for line in read:
            currentline = line.split(",")
        inventory = add_to_inventory(inventory, currentline)
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    outputlist = []
    for key in inventory:
        value = 0
        while value < inventory[key]:
            outputlist.append(key)
            value += 1
    with open(filename, "w", newline="") as outputstream:
        writer = csv.writer(outputstream)
        writer.writerow(outputlist)

print_table()