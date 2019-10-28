"""try:
    a=open('fan1.in')
    print(a.read())
finally:
    if a:
        a.close()
"""
from io import StringIO,BytesIO
import pickle
a=dict(a=0,b='sb')
for x,y in a.items():
    print(x,y)
"""f=StringIO('hello hello')
a=BytesIO()
a.write("中文".encode('utf-8'))
print(a.getvalue())
f.write('hello')
print(f.getvalue())
print(f.read())"""

