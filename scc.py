import requests
import colorama
from colorama import Fore, Style

api_base = 'https://universalis.app/api/'
api_server = ''

job = [
    'ALC', 'ARM', 'BSM', 'CRP', 'CUL', 'GSM', 'LTW', 'WVR'
]

# Material, Id, Number
# Palm Sugar, 36080, 0
# Sykon, 36096, 1
# Ovibos Milk, 36255, 2
# Chondrite Ingot, 36172, 3
# Star Quartz. 36186, 4
# Integral Lumber, 36200, 5
# Ophiotauraos Leather, 36251, 6
# Ar-Caean Velvet, 36212, 7
# Enchanted Manganese Ink, 36238, 8

materialID = [
    '36080',
    '36096',
    '36255',
    '36172',
    '36186',
    '36200',
    '36096',
    '36212',
    '36238'
]
materialName = [
    'Palm Sugar',
    'Sykon',
    'Ovibos Milk',
    'Chondrite Ingot',
    'Star Quartz',
    'Integral Lumber ',
    'Ophiotauraos Leather ',
    'Enchanted Manganese Ink ',
]

materialPrice = [
]

materialCheapest = [0, 0, 0, 0, 0, 0, 0, 0, 0
                    ]
worlds = [
    'lich',
    'odin',
    'phoenix',
    'shiva',
    'zodiark',
    'twintania'
]


index = 0
for world in worlds:
    print()
    print(Fore.BLUE + 'Querying %s prices.' % worlds[index])
    for material in materialID:
        api_server = worlds[index]
        response = requests.get(
            api_base+api_server+'/'+material)

        resp = response.json()

        if len(materialPrice) <= 8:
            materialPrice.append(resp['currentAveragePriceNQ'])
        else:
            if materialPrice[index] > resp['currentAveragePriceNQ']:
                materialPrice[index] = resp['currentAveragePriceNQ']
                materialCheapest[index] = index
    print(Fore.GREEN + 'Done.')
    index = index + 1


# recipes calculation
recipe = []
# ALC
recipe.append(materialPrice[8] + materialPrice[4] +
              materialPrice[6] + materialPrice[6])
# ARM
recipe.append(materialPrice[6]+materialPrice[4] +
              materialPrice[3]+materialPrice[3])
# BSM
recipe.append(materialPrice[6]+materialPrice[5] +
              materialPrice[3]+materialPrice[3])
# CRP
recipe.append(materialPrice[6]+materialPrice[4] +
              materialPrice[4]+materialPrice[3])
# CUL
recipe.append(materialPrice[0]+materialPrice[0] +
              materialPrice[0]+materialPrice[1]+materialPrice[2]+10)
# GSM
recipe.append(materialPrice[7]+materialPrice[4] +
              materialPrice[4]+materialPrice[3])
# LTW
recipe.append(materialPrice[6]+materialPrice[6] +
              materialPrice[7]+materialPrice[3])
# WVR
recipe.append(materialPrice[7]+materialPrice[7] +
              materialPrice[6]+materialPrice[4])

print()
print()
print('The cheapest 500 purple scrip costs about %d GIL and is made by %s .' %
      (min(recipe)*500/144, job[recipe.index(min(recipe))]))
print()
print(Fore.MAGENTA + 'Shopping List')
print()

match  recipe.index(min(recipe)):
    case 0:
        print('Buy Enchanted Manganese Ink on %s .' %
              worlds[materialCheapest[8]])
        print('Buy Star Quartz %s .' % worlds[materialCheapest[4]])
        print('BuyOphiotauraos Leather on %s .' % worlds[materialCheapest[6]])
    case 1:
        print('Buy Chondrite Ingot on %s .' % worlds[materialCheapest[3]])
        print('Buy Star Quartz %s .' % worlds[materialCheapest[4]])
        print('BuyOphiotauraos Leather on %s .' % worlds[materialCheapest[6]])
    case 2:
        print('Buy Chondrite Ingot on %s .' % worlds[materialCheapest[3]])
        print('Buy Integral Lumber on %s .' % worlds[materialCheapest[5]])
        print('BuyOphiotauraos Leather on %s .' % worlds[materialCheapest[6]])
    case 3:
        print('Buy Chondrite Ingot on %s .' % worlds[materialCheapest[3]])
        print('Buy Star Quartz %s .' % worlds[materialCheapest[4]])
        print('BuyOphiotauraos Leather on %s .' % worlds[materialCheapest[6]])
    case 4:
        print('Buy Palm Sugar on %s .' % worlds[materialCheapest[0]])
        print('Buy Sykon on %s .' % worlds[materialCheapest[1]])
        print('Buy Ovibos Milk on %s .' % worlds[materialCheapest[2]])
    case 5:
        print('Buy Chondrite Ingot on %s .' % worlds[materialCheapest[3]])
        print('Buy Star Quartz %s .' % worlds[materialCheapest[4]])
        print('Ar-Caean Velvet on %s .' % worlds[materialCheapest[7]])
    case 6:
        print('Buy Chondrite Ingot on %s .' % worlds[materialCheapest[3]])
        print('BuyOphiotauraos Leather on %s .' % worlds[materialCheapest[6]])
        print('Ar-Caean Velvet on %s .' % worlds[materialCheapest[7]])
    case 7:
        print('Buy Star Quartz %s .' % worlds[materialCheapest[4]])
        print('BuyOphiotauraos Leather on %s .' % worlds[materialCheapest[6]])
        print('Ar-Caean Velvet on %s .' % worlds[materialCheapest[7]])
print()
print()
