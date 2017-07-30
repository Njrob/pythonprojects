stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):#, addedItems):
    print("Inventory:")
    item_total = 0
    #for i in addedItems:
 #       inventory.setdefault(i, 0)
 #       inventory[i] += 1
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)#, dragonLoot)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    item_total = 0
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] += 1
    return inventory

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)


