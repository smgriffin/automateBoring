# Fantasy game inventory

inventory = {'rope': 1, 'torch': 2, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inv):
    print('Inventory:')
    itemQuantity = 0
    for k, v in inventory.items():
        itemQuantity = itemQuantity + inventory.get(k, 0)
        print(str(v) + ' ' + str(k))
    print('Total number of items: ', end='' + str(itemQuantity))


def addToInventory(inv, addedItems):
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i], 1)
        inv[addedItems[i]] = inv[addedItems[i]] + 1
        global inventory
        inventory = inv


addToInventory(inventory, dragonLoot)
displayInventory(inventory)
