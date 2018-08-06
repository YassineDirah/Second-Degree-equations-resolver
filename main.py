def main():

    print("ax²+bx+c=0")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    delta = (b ** 2) - (4 * a * c)

    if delta == 0:

        x = round((-b) / (2 * a), 2)
        print("x ={} \n".format(x))
        main()

    elif delta > 0:

        s1 = round((-b - (delta ** 0.5)) / (2 * a), 2)
        s2 = round((-b + (delta ** 0.5)) / (2 * a), 2)
        print("s1 ={}\ns2 ={}".format(s1,s2))
        main()

    else:

        print("This equation has not a solution in R \n")
        main()

if __name__ == '__main__':main()
