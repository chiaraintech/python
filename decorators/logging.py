#Logging (when not using the logging module)

def logged(function):
    def wrapper(*args, **kwargs):
        value=function(*args, **kwargs)
        with open('logfile.txt','a+') as f:
            fname = function.__name__
            f.write(f"{fname} return value: {value}")
        return value

    return wrapper

@logged
def add(x, y):
    return x + y

sum = add(10,20)

print(sum)