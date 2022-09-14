richter_values = [1, 5, 9.1, 9.2, 9.5]
print('Richter      Joules                  TNT')

def joules(richter):
    calc1 = (1.5 * float(richter)) + 4.8
    calc2 = 10 ** calc1
    return calc2

def tnt(joules):
    return joules / (4.184*(10**9))

for values in richter_values:
    print (f'{values}       {joules(values)}        {tnt(joules(values))}')

richter_input = float(input('Enter richter value: '))

print(f'Richter value {richter_input} \nEquivalence in joules: {joules(richter_input)} \nEquivalence in tons of TNT: {tnt(joules(richter_input))}')
