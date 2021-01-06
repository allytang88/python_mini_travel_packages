import csv
from datetime import datetime, timedelta

#Part 1- Set data 

#Prices for packages and tickets
cruise_price = 250
island_price = 200
spa_price = 150
hiking_price = 80

#Peak ticket is 20% more expensive than nonpeak ticket
nonpeak_ticket = 1
peak_ticket = 1.2

#Children ticket is 50% discount and senior ticket is 20% discount from adult ticket
child_discount = .50
adult_price = 1
senior_discount = .80

  


#Part2 -Display headings and package information
def info_header():
    
    print("      *************************")
    print("      Welcome to SA tour agency")
    print("      *************************")
    print("\n")
    print("      ***Packages Information***\n")
    print(" ** Cruise package is $250 per pax **\n","** Island package is $200 per pax **\n","** Spa package is $150 per pax **\n","** Hiking packages is $80 per pax **\n")
    print(" ** Full price for Weekdays **\n","** Additional 20% for Weekends or Public Holidays **\n")
    print(" ** Children ticket is 50% discount **\n","** Senior ticket is 20% discount **") 
    print("\n")
    print("Please choose your options!\n")

#Part 3- All the functions created

def current_date():

    from datetime import datetime, timedelta
    today = datetime.now()
    timestampStr = today.strftime("%d-%b-%Y (%H:%M)")
    print("Today date is : " + str(timestampStr))
    

    
def under_budget():
    print("****Thank you choosing this selection, you are within your budget****")
        
def over_budget():
    print("****This package exceeded your budget, \n","please consider our off-peak as well as cheaper packages that are available***")
        
    
def package_dates_selection():
    if package == "1":
        print("You have choosen option: ",str(package),"for Cruise Package")
        if str(date) == "1":
            print("You have choosen option: ",str(date),"for Non-peak season")
        else:
            print("You have choosen option: ",str(date),"for Peak season")
        dates_selection()
        print("Total number of pax is : ",total_pax)
        
    elif package == "2":
        print("You have choosen option: ",str(package),"for Island Package")
        if str(date) == "1":
            print("You have choosen option: ",str(date),"for Non-peak season")
        else:
            print("You have choosen option: ",str(date),"for Peak season")        
        dates_selection()
        print("Total number of pax is : ",total_pax)
    elif package == "3":
        print("You have choosen option: ",str(package),"for Spa Package")
        if str(date) == "1":
            print("You have choosen option: ",str(date),"for Non-peak season")
        else:
            print("You have choosen option: ",str(date),"for Peak season")
        dates_selection()
        print("Total number of pax is : ",total_pax)
    else:
        print("You have choosen option: ",str(package),"for Hiking Package")
        if str(date) == "1":
            print("You have choosen option: ",str(date),"for Non-peak season")
        else:
            print("You have choosen option: ",str(date),"for Peak season")
        dates_selection()
        print("Total number of pax is : ",total_pax)
        

def dates_selection():
    print("You are buying for :",str(no_pax_child),"-children tickets,",str(no_pax_adult),"-Adult tickets, and",str(no_pax_senior),"-Senior tickets")

def cal_package():           
    #Calculation of number of pax and amount for different packages
                                            
    total_pax = (int(no_pax_adult))+(int(no_pax_child))+(int(no_pax_senior))
    total_amount_pax = (int(no_pax_adult))+((int(no_pax_child)) * child_discount)+((int(no_pax_senior)) * senior_discount) 
                
    c_NP = (cruise_price * nonpeak_ticket * total_amount_pax) 
    i_NP = (island_price * nonpeak_ticket * total_amount_pax)
    s_NP = (spa_price * nonpeak_ticket * total_amount_pax)
    h_NP = (hiking_price * nonpeak_ticket * total_amount_pax)
    c_P = (cruise_price * peak_ticket * total_amount_pax)
    i_P = (island_price * peak_ticket * total_amount_pax)
    s_P = (spa_price * peak_ticket * total_amount_pax)
    h_P = (hiking_price * peak_ticket * total_amount_pax)  
                        
 
    if package == str(1):
        if date == str(1):
            current_date()
            package_dates_selection()
            print("The total amount you need to pay is $", round(float((c_NP)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(c_NP) <= float(budget_input)):
                under_budget()
            else:
                over_budget()
        elif date == str(2):
            current_date()
            package_dates_selection()       
            print("The total amount you need to pay is $",round(float((c_P)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(c_P) <= float(budget_input)): 
                under_budget()
            else:
                over_budget()
        else:
            print("You have enter a wrong selection in date selection!")    
    elif package == str(2):
        if date == str(1):
            current_date()
            package_dates_selection()        
            print("The total amount you need to pay is $",round(float((i_NP)),2))
            print("Your input budget is : $",(float(budget_input)))
            if (float(i_NP) <= float(budget_input)):
                under_budget()
            else:
                over_budget()
        elif date == str(2):
            current_date()
            package_dates_selection()       
            print("The total amount you need to pay is $",round(float((i_P)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(i_P) <= float(budget_input)):
                under_budget()
            else:
                over_budget()
        else:
            print("You have enter a wrong selection in date selection!")      
    elif package == str(3):
        if date == str(1):
            current_date()
            package_dates_selection()       
            print("The total amount you need to pay is $",round(float((s_NP)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(s_NP) <= float(budget_input)): 
                under_budget()
            else:
                over_budget()
        elif date == str(2):
            current_date()
            package_dates_selection()       
            print("The total amount you need to pay is $",round(float((s_P)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(s_P) <= float(budget_input)):
                under_budget()
            else:
                over_budget()
        else:
            print("You have enter a wrong selection in date selection!")    
    elif package == str(4):
        if date == str(1):
            current_date()
            package_dates_selection()       
            print("The total amount you need to pay is $",round(float((h_NP)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(h_NP) <= float(budget_input)):
                under_budget()
            else:
                over_budget()
        elif date == str(2):
            current_date()
            package_dates_selection()       
            print("The total amount you need to pay is $",round(float((h_P)),2))
            print("Your input budget is : $",float(budget_input))
            if (float(h_P) <= float(budget_input)):
                under_budget()
            else:
                over_budget()
        else:
            print("You have enter a wrong selection in date selection!")    
    elif package != (str(1) or str(2) or str(3) or str(4)):
        print("You have enter a wrong selection in packages!")



#Show option available
def showoptions():
    #Display Header Information calling function
    info_header()    
    #print("\n")
    print("------------------------------")
    print("B. Check your previous booking")
    print("C. Enter your details")
    print("Q. Quit")
    
  
#check previous booking
showoptions()
option = input("Please select option : ")


while option != "Q":
    # option 1 check booking
        if option == "B":
        # get booking id/email from user
            idemail = input("Please enter your cust id or email:")
            print("------")
    
            # if booking id/email is not given, show error
            if idemail is None:
                print("Error: please enter a valid booking id or email.")
            else:
                #get data from file
                with open('SA_tour_agency1.csv', 'r') as file:
                    reader = csv.reader(file)
    
                    for row in reader:
                        if(row[0] == idemail or row[8] == idemail):
                            #display booking details
                            print("Here are your booking details:\nCust id: " + row[0] + "\nUser Name: " + row[1] + "\nBudget: $" + row[2] + "\nChild ticket: " + row[3] + "\nAdult ticket: " + row[4] + "\nSenior ticket: " + row[5] + "\nPackages: " + row[6] + "\nWeekdays/Weekends: " + row[7] + "\nEmail: " + row[8] + "\nBooking time: " + row[9])
                            break
                    # if booking id is not found, do this
                    else:
                            print("Error: Booking not found. Please contact us if you have any issues.")
                    file.close()
                    
                    
                    
        elif option == "C":
            #Part 4- Read and write data from/to file
            today = datetime.now()
            timestampcsv = str(today.strftime("%d-%b-%y %H:%M %p"))        
            with open('SA_tour_agency1.csv', 'r', newline = '') as file:
                reader = csv.reader(file)
                lines = len(list(reader))
                
                #cust id auto generate
                custid = int(lines)
            
                # Enter your user input section
                    
                        
                while True:
                    try:            
                        user_name = input("Please enter your name : \n")
                        email_address = input("Please enter your email address : \n")            
                        budget_input = int(input("Enter your budget: \n"))
                        no_pax_child = int(input("Enter the number of passengers for children below 12 years old : \n"))
                        no_pax_adult = int(input("Enter the number of passengers for adult from 12 to 60 years old : \n"))
                        no_pax_senior = int(input("Enter the number of passengers for senior above 60 years old : \n"))
                        package = input("Enter 1 for 'Cruise', 2 for 'Island Tour', 3 for Spa tour, 4 for hiking tour: \n")
                        
                        break
                    except ValueError:
                        print("Error: please enter numbers only.")
                        continue    
               
      
                date = input("Enter your travel date, 1 for weekdays or 2 for weekends/public holidays : \n")
                    
                total_pax = (int(no_pax_adult))+(int(no_pax_child))+(int(no_pax_senior))
                total_amount_pax = (int(no_pax_adult))+((int(no_pax_child)) * child_discount)+((int(no_pax_senior)) * senior_discount) 
                            
                c_NP = (cruise_price * nonpeak_ticket * total_amount_pax) 
                i_NP = (island_price * nonpeak_ticket * total_amount_pax)
                s_NP = (spa_price * nonpeak_ticket * total_amount_pax)
                h_NP = (hiking_price * nonpeak_ticket * total_amount_pax)
                c_P = (cruise_price * peak_ticket * total_amount_pax)
                i_P = (island_price * peak_ticket * total_amount_pax)
                s_P = (spa_price * peak_ticket * total_amount_pax)
                h_P = (hiking_price * peak_ticket * total_amount_pax)                          
                
                from datetime import datetime, timedelta
                today = datetime.now()
                        
                #write booking details into file
                with open('SA_tour_agency1.csv', 'a', newline = '') as file:
                    writer = csv.writer(file)
                    writer.writerow([custid, user_name, budget_input, no_pax_child, no_pax_adult, no_pax_senior, package,date, email_address,today])
    
                print("------")
                print("Thank you for booking with SA tour Agency!")
                print("------")
                file.close()
                cal_package()
        else:
            if option == "Q":
                print("You have Quit the program")
        showoptions()
        option = input("Please select option:")
        print("------")                          

    
            
   