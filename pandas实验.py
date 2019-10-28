from pandas import Series,DataFrame
import pandas as pd
import numpy as np
obj=Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
obj2=obj.reindex(['a','b','c','d','e'])
obj3=Series(['blue','purple','yellow'],index=[0,2,4])
print(obj3)
obj4=obj3.reindex(range(6),method='ffill')
print(obj4)
frame=DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns\
                =['ohio','Texas','california'])
print(frame)
frame2=frame.reindex(['a','b','c','d'])
print(frame2)
frame3=frame.reindex(columns=['Texax','Utah','california'])
print(frame3)