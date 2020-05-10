# AISaturdaysAbeokuta2020

## Assignment
Fork this git repository, then clone it on your computer
https://github.com/kcemenike/AISaturdaysAbeokuta2020.git

If you have any issues, please visit this help guide (for Github desktop)
https://help.github.com/en/desktop/contributing-to-projects/cloning-and-forking-repositories-from-github-desktop
https://help.github.com/en/github/getting-started-with-github/fork-a-repo

Do the tasks below
1. Accept input from user in the format DD-MM-YYYY (e.g. 21-03-1990) and compute age in days
2. edit the code so that the user can always restart the code execution
In the input, ask the user to type 0 to exit or his date of birth
- If user types 0, exit the program
- If user types his date of birth, compute the age
- After age computes, give the opportunity to the user to enter another date of birth

### Update:

Once done with the edits in your clone, please commit your code to your repo, then reach out to me in the contact detail below where I'll create a branch for you to do a pull request  into, and I can review your submission

If you have any issues, kindly reach out via Twitter (@kcemenike or @pydataco), Telegram (@pydataco) or via email (kcemenike [at] live [dot] com)

# Cheers!!!

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

