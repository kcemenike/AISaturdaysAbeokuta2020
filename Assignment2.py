def computeAge():
    
    
    while True:
        from datetime import datetime
        #get input from user
        user_input = input("Please enter input in the format dd-mm-yy or '0' to end the program>>> "  )
      
        #break out of loop if user enter '0'
        if  user_input == '0':
            print("You ended the program,thank you for your time.")
            break
        else:
            try:
                present_day = datetime.today()
        
                date_of_birth = datetime.strptime(user_input, '%d-%m-%Y')
                
                days_of_birth = date_of_birth
        
       
       
                #calculating age in days from data given
                age = present_day - days_of_birth
                print("You age in days so far on earth is:", age.days)
                continue
                
             
            except ValueError:
                print("Please, input in the correct format")
            
                
            
             
            
            
computeAge()
        
                
    
    
       