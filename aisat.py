def age_calculator():
    import datetime
    while True:
        # Get input or 0
        input_value = input(
            "Please enter your date of birth in the format dd-mm-yyyy or enter 0 to exit")
        # break out of loop if input is 0
        if input_value == '0':
            print("You have now exited the application")
            break
        else:
            try:
                date_of_birth_date = datetime.datetime.strptime(
                    input_value, '%d-%m-%Y')
            except ValueError:
                print("You have entered the date in a wrong format or you have entered an invalid date\nPlease try again in this format: dd-mm-yyyy")
            else:
                currentYear = datetime.datetime.now().year
                year_of_birth = date_of_birth_date.year
                age = currentYear - year_of_birth
                print(f"Your current age is {age}")
                return age


age_calculator()

''' Assignment update
Fork this git repository, then clone it on your computer
https://github.com/kcemenike/AISaturdaysAbeokuta2020.git

If you have any issues, please visit this help guide (for Github desktop)
https://help.github.com/en/desktop/contributing-to-projects/cloning-and-forking-repositories-from-github-desktop
https://help.github.com/en/github/getting-started-with-github/fork-a-repo
'''
