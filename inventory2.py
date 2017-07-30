inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
              
    
addToInventory(inv, dragonLoot)
