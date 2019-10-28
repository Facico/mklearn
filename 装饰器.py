"""def log(f):
    def wrapper(*args,**kw):
        print('call %s():' % f.__name__)
        return f(*args,**kw)
    return wrapper
@log#在log中返回wrapper，参数是now()
def now():
    print('2015-3-25')
now()"""
"""def wrapper(*args, **kw):
    print('call %s():')
    return now(*args, **kw)
a=wrapper(1)"""
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()