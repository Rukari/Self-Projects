import time
people = ["anjuvh", "cj", "over"]
weight = [46, 100, 200]
hegiht = [1.68, 1.70, 1.70]#in meters
f = open("BMI Database.py", "w")

def acc():
    try:
        print("")
        time.sleep(1)
        n = input("Enter name: ").strip().lower()
        i = people.index(n)
        time.sleep(1)
        print(people[i])
        time.sleep(1)
        print("weight(kg): ", weight[i])
        time.sleep(1)
        print("Height(m): ", hegiht[i])
        time.sleep(1)
        BMI = weight[i] / (hegiht[i]*2)
        print("BMI: ", BMI)
        time.sleep(1)
        if BMI <= 18.5:
            print("Your Underweight")
        elif 18.5 <= BMI <= 24.9:
            print("You are normal")
        elif 25 <= BMI <= 29.9:
            print("You are Overweight")
        elif 30 <= BMI <= 34.9:
            print("Overweight Class 1")
        elif 35 <= BMI <= 39.9:
            print("You are Obesity Class 2")
        else:
            print("You are Extreme Obesity")
        time.sleep(5)
        print("Going back to menu....")
        time.sleep(3)
        main()

    except ValueError:
        time.sleep(1)
        print("U dont have a BMI")
        print("Going back to menu....")
        time.sleep(2)
        main()

def main():
    try:
        print("")
        time.sleep(1)
        print("(1)Check your BMI")
        time.sleep(1)
        print("(2)Make a BMI")
        time.sleep(1)
        print("(3)End")
        time.sleep(1)
        a = input(": ").strip()
        if a == "1":
            acc()
        elif a == "2":
            make()
        elif a =="3":
            exit()
        else:
            print("Please select the right choices")
            main()


        print("")

    except ValueError:
        print("Please select the right choices")
        make()


def make():
    try:
        print("")
        time.sleep(1)
        p = input("Enter name: ")
        time.sleep(1)
        w = float(input("Enter weight(kg): "))
        time.sleep(1)
        h = float(input("Enter height(m): "))
        time.sleep(1)
        people.append(p)
        weight.append(w)
        hegiht.append(h)
        print("Saving...")
        time.sleep(2)
        print("Going back to menu....")
        time.sleep(2)
        f.write("people =" + str(people))
        f.write("weight =" + str(weight))
        f.write("hegiht =" + str(hegiht))
        f.close()
        main()

    except ValueError:
        print("Inster correct given")
        make()

main()