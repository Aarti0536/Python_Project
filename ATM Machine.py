#!/usr/bin/env python
# coding: utf-8

# # WAP for ATM machine

# In[ ]:


acc_num = [23453,34543,97866,57745]
acc_bal = [10000,8000,9000,5500]

acc_num_send= [76567,34536,75895,35756]
acc_bal_send = [5000,3000,12000,4000]

acc_pin = [123,543,878,956]

while True:
    print("Welcome to ATM machine")
    enter_acc_num = int(input("Enter Account number = "))
    enter_pin = int(input("Enter Your Pin = "))
    
    if(enter_acc_num in acc_num and enter_pin in acc_pin):
        acc_index = acc_num.index(enter_acc_num)
        
        if (enter_pin == acc_pin[acc_index]):
            print("select any opeartion")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. check Balance")
            print("4. Transer Money")
            
            choice = int(input("Enter your choice = "))
            
            if choice == 1:
                deposit = int(input("Enter amount to deposit = "))
                if(deposit >0):
                    acc_bal[acc_index] += deposit
                    #deposit = acc_bal[acc_index] + deposit
                    print("Amount deposit Successfull = ",acc_bal[acc_index])
                else: print("Failed")
                    
            elif (choice == 2):
                withdraw_amount = int(input("Enter amount you want to withdraw = "))
                if(withdraw_amount <= acc_bal[acc_index]):
                                      acc_bal[acc_index] -= withdraw_amount
                                      #withdraw_amount = acc_bal[acc_index] - withdraw_amount
                        
                                      print("Amount Withdraw successfull = ",acc_bal[acc_index])
                else:
                    print("Sorry ! you cann't withdraw because Entered amount is greater than account balance")
                    
            elif(choice == 3):
                print("Account Number is = ",acc_num[acc_index])
                print("Account balance is = ", acc_bal[acc_index])
                
            elif(choice == 4):
                enter_acc_num_send= int(input("Enter Account number in which you want to transfer money = "))
                send_amount = int(input("How much amount you want to send = "))
                transer_index = acc_num_send.index(enter_acc_num_send)
                receiver_bal = acc_bal_send[transer_index] + send_amount
                sender_bal = acc_bal[acc_index] - send_amount
                print("The total amount in sender's account is = ",sender_bal)
                print("The total amount in reciver's account is = ",receiver_bal)
            else:
                print("Invalid Choice")
    else:
        print("Invalid ATM pin")
    repeat = input("Do you want to repeat yes or no = ")
    if(repeat == "yes"):
        continue
    else:
        print("Thank you for visiting ATM machine")
        break


    
                     
                
                
                    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




