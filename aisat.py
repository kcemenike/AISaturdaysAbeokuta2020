def compute_age_from_dob(year_of_birth='1900'):
    '''This function computes the age when a user enters
    a year of birth
    '''
    # John: subtract the current year from the input year
    # Get current year from datetime
    import datetime
    currentYear = datetime.datetime.now().year  # datetime.datetime.today().year

    # Get year of birth from user
    year_of_birth = input("Please enter your year of birth")
    # convert year_of_birth to integer
    # implement try except block for converting string to int
    try:
        year_of_birth_int = int(year_of_birth)
        # year_of_birth = int(input("Please enter your year of birth"))
    except ValueError:
        print("You have not entered your year of birth in the format 19XX\n")
    else:
        age = currentYear - year_of_birth_int
        print(f"You are {age} years old")  # f-string works after Python 3.5
        # print("You are {} years old".format(age)) # before Python 3.5
    pass


compute_age_from_dob()

''' Assignment update
Fork this git repository, then clone it on your computer
https://github.com/kcemenike/AISaturdaysAbeokuta2020.git

If you have any issues, please visit this help guide (for Github desktop)
https://help.github.com/en/desktop/contributing-to-projects/cloning-and-forking-repositories-from-github-desktop
https://help.github.com/en/github/getting-started-with-github/fork-a-repo

Do the tasks below
1. Accept input from user in the format DD-MM-YYYY (e.g. 21-03-1990) and compute age
2. edit the code so that the user can always restart the code execution
In the input, ask the user to type 0 to exit or his date of birth

    If user types 0, exit the program
    If user types his date of birth, compute the age
    After age computes, give the opportunity to the user to enter another date of birth
'''
