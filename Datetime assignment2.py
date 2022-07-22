def compute_age():
    while True:
        #get the age of users by getting informations needed#
        from datetime import datetime
        dob = input('enter your date of birth in the format "dd-mm-yyyy":')
        value = dob
        try:
        #this gets the users date of birth, after that get the current date#
            todaysDate = datetime.today()
            date_of_birth = datetime.strptime(dob, '%d-%m-%Y')
        #calculate age with data available#
            age = todaysDate - date_of_birth
            print('Your age in days:', age.days)
            continue
        except:
            dob == 0
            print('code didnot run because of wrong user input and has ended')
            break
        return age
compute_age()

