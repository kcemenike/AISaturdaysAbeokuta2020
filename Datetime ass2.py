def compute_age():
    code_run = True
    while True:
        #get the age of users by getting informations needed#
        from datetime import datetime
        dob = input('enter your date of birth in the format "dd-mm-yyyy":')
        if dob == '0':
            code_run = False
            print('code has ended')
            break
        try:
        #this gets the users date of birth, after that get the current date#
            todaysDate = datetime.today()
            date_of_birth = datetime.strptime(dob, '%d-%m-%Y')
        #calculate age with data available#
            age = todaysDate - date_of_birth
            print('Your age in days:', age.days)
            continue
        except ValueError:
            print('invalid input')
            continue
        return age
compute_age()

