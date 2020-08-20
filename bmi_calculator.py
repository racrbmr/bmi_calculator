#   creating BMI Calculator for my first project #
# ################################################

# ############ v.2 ###############
# -fix the output number 'too long'
# -add repeat process
# -simplified code(input)

# calculate function


def calculate():
    #   getting input from user
    weight = int(input("input your weight: "))
    height = float(input("input your height: "))
    #   calculate
    result = weight / (height/100)**2
    #   condition
    if result == 15:
        print("Your BMI category is 'Very severely underweight'" +
              " BMI: " + str(result)[0:4])
    elif 15 <= result <= 16:
        print("Your BMI catergory is 'Severely underweight" +
              " BMI: " + str(result)[0:4])
    elif 16 <= result <= 18.5:
        print("Your BMI catergory is 'Underweight'" +
              " BMI: " + str(result)[0:4])
    elif 18.5 <= result <= 25:
        print("Your BMI catergory is 'Normal (healthy weight)'" +
              " BMI: " + str(result)[0:4])
    elif 25 <= result <= 30:
        print("Your BMI catergory is 'Overweight'" +
              " BMI: " + str(result)[0:4])
    elif 30 <= result <= 35:
        print("Your BMI catergory is 'Moderately obese'" +
              " BMI: " + str(result)[0:4])
    elif 35 <= result <= 40:
        print("Your BMI catergory is 'Severely obese'" +
              " BMI: " + str(result)[0:4])
    elif result > 40 and result <= 100:
        print("Your BMI catergory is 'Very severely obese'" +
              " BMI: " + str(result)[0:4])
    else:
        print("i'm sorry but your BMI is too high :(")


#   call the function
calculate()


# BMI calculation formula reference : https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php
# racrbmr@github
# licensed under The Unlicense
