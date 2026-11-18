# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
<<<<<<< HEAD
    if b == 0:
        return 'Cannot divide by zero'
=======
>>>>>>> 5c1199a5755bf9000b72692f7222e6ca1ce69f5a
    return a / b

def main():
    print('Add:', add(5, 3))
    print('Subtract:', subtract(5, 3))

if __name__ == '__main__':
    main()