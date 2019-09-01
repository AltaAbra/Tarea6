#return the absolute value of a number

def abs(num):
    return num *-1 if num<0 else num #operador ternario
    #return number<0 ? numb *-1 : num
    
def main():
    print(abs(0))
    print(abs(-3))
    print(abs(10))

if __name__ == "__main__":
    main()

