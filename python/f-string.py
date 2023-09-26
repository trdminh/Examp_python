person = 'Minh'
coins = 3
print(person + " has " + str(coins) + ' coins left.')
player = {'person':'Minh','coins':3}
mess = "\n{person} has {coins} coins left.".format(**player)
print(mess)
mess = f"\n{person} has {coins} coins left."
print(mess)