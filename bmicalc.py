##building a BMI calculator

'''
 BMI = (weight in pounds * 703)/ (height * height) in inches
 <18 underweight, minimal
 18-24.9 normal weight, minimal
 25-29.9 overweight, increased
 30-34.9 obese high, high
 35-39.9 severly ,obese very high
 40+ morbidly obese ,extremely high
'''
name = input("Enter Your Name: ")
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in Inches: "))


def calc_bmi(weight, height):
    weight = float(weight)
    height = float(height)
    bmi = (weight * 703) / (height * height)
    return bmi

def main(name):
    answer = calc_bmi(weight, height)
    if answer < 18:
        print(f"Hello {name} Your BMI is {answer},\n Your are underweight \n There is a minimal Health risk")
    elif answer >= 18 and answer < 25:
        print(f"Hello {name} Your BMI is {answer},\n Your are normal weight \n There is a minimal health risk")
    elif answer >= 25 and answer < 30:
        print(f"Hello {name} Your BMI is {answer},\n Your are overweight \n There is an increased health risk")
    elif answer >= 30 and answer < 35:
        print(f"Hello {name} Your BMI is {answer},\n Your are obese \n There is a high health risk")
    elif answer >40:
        print(f"Hello {name} Your BMI is {answer},\n its a morbidity obese \n There is an extremely health risk")
    else:
        print("There was an error in some place")


main(name) 

