import pandas as pd
#table
data = {
        'Load': ['L2', 'L2', 'L3', 'L4'],
        'Voltage': [230, 225, 240, 218 ],
        'Current(A)': [5, 8, 6, 10 ]
        }

table = pd.DataFrame(data)

print(table)

