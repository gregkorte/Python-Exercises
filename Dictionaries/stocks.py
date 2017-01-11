'''
PART I
'''
stockDict = {'GM': 'General Motors', 'CAT': 'Caterpillar', 'EK': 'Eastman Kodak'}

purchases = [ ('GE', 100, '10-Sep-2001', 48), ('CAT', 100, '1-Apr-1999', 24), ('GE', 200, '1-Jul-1998', 56) ]

for purchase in purchases:
    cost = purchase[1] * purchase[3]
    if purchase[0] in stockDict:
            print(stockDict[purchase[0]] + ': $' + str(cost)  + '\n')

'''
PART II
'''
summary = dict()
for purchase in purchases:
    cost = purchase[1] * purchase[3]
    summary[purchase[0]] = cost
    if purchase[0] in summary:
        summary[purchase[0]] += cost
print(summary)