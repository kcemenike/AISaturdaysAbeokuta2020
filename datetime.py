def compute_age():
    while True:
        from datetime import datetime
        
        dob = input("Please enter your date of birth this way 'dd-mm-yyyy': ")
        
        answer = dob
        try:
            
            calculation = datetime.today().toordinal() - datetime.strptime(dob, "%m-%d-%Y").toordinal()
            
            currentAge = int(datetime.fromordinal(calculation).strftime("%Y"))
            
            
            if answer == dob:
                  print(f"You are {currentAge} years old.")
            continue
            
        except ValueError:
            if dob == "0":
                 print("You ended the program yourself by pressing '0' ")
                 break
         
    
compute_age()