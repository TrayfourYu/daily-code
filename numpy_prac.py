import numpy as np


a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # 判定a大于2的结果矩阵

print (bool_idx)     # Prints [[False False]
                    #          [ True  True]
                    #          [ True  True]]"

# 再通过bool_idx取出我们要的值
print (a[bool_idx])# Prints "[3 4 5 6]"

# 放在一起我们可以这么写
print (a[a > 2])
# Prints "[3 4 5 6]"
