#   creating BMI Calculator for my first project #
# ################################################

# ############ v.1 ###############

#   getting input from user
weight = input("input your weight: ")
height = input("input your height: ")

#   changing var type
weight = int(weight)
height = int(height)


#   calculate the inputs
def calculate():
    result = weight / (height/100)**2
    if result == 15:
        print("Your BMI category is 'Very severely underweight'" +
              " BMI: " + str(result))
    elif 15 <= result <= 16:
        print("Your BMI catergory is 'Severely underweight" +
              " BMI: " + str(result))
    elif 16 <= result <= 18.5:
        print("Your BMI catergory is 'Underweight'" +
              " BMI: " + str(result))
    elif 18.5 <= result <= 25:
        print("Your BMI catergory is 'Normal (healthy weight)'" +
              " BMI: " + str(result))
    elif 25 <= result <= 30:
        print("Your BMI catergory is 'Overweight'" +
              " BMI: " + str(result))
    elif 30 <= result <= 35:
        print("Your BMI catergory is 'Moderately obese'" +
              " BMI: " + str(result))
    elif 35 <= result <= 40:
        print("Your BMI catergory is 'Severely obese'" +
              " BMI: " + str(result))
    elif result > 40 and result <= 100:
        print("Your BMI catergory is 'Very severely obese'" +
              " BMI: " + str(result))
    else:
        print("i'm sorry but your BMI is too high :(")


#   call the function
calculate()


# BMI calculation formula reference : https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php
# racrbmr@github
# license under The Unlicense
