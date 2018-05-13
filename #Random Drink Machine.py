# Random Drink Machine

print('Hello There, please enter your Name')
name = input()

print(name + 'you have the choice of alcohol, supplements will be random choiced')
alcohol = ['Vodka', 'Gin', 'Bacardi', 'Havanna 7 Anos']
supplements = ['Tonic Water', 'Coke', 'Sprite', 'Champagne']

print(alcohol)
print('Wähle zwischen 0 und 3 ;-)')
i = str(input())
print(alcohol[input()] + supplements)
