def func (num):
    string = str(num)
    if len(string)>3:
        raise IndexError()
    a= int(string[0])
    b=int(string[1])
    c=int(string[2])
    return a+b+c, a*b*c


#func(3388)
