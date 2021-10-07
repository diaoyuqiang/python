import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

# 通过关键字key，合并left和right
res = pd.merge(left, right, on='key')
print(res)