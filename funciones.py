def square(x):
    return x*x
def main():
    for i in range (10):
        print("{} square is {}".format(i,square(i)))
        #esta es una notacion media vieja
if __name__=="__name__":
    main()
    #solo corre main si la llamo especificamente y no cuando imporo una funcion
