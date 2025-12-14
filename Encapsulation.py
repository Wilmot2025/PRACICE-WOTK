
class Bank:
  bank_name = "ECO"
  account_number = "167886766"
  bank_balance = "10000000"

  def Wil_bank_info (myself):# public method
    print("Bank name is",myself.bank_name)# public method
    print("Account number is",myself.account_number) # public method
    print("Bank balance is",myself.bank_balance) # public method 

    bank_obj = Bank()
    bank_obj.Wil_bank_info()
    bank_obj.bank_name
    bank_obj.account_number
    bank_obj.bank_balance
     

class House:  
  house_name = "Mansion"
  house_price = "20,000"
  house_location = "Liberia"

  def house_info (myself): # public method
   print("House name is",myself.house_name)# public method
   print("House price is",myself.house_price)
   print("House location is",myself.house_location)

  house_obj = House()       
  house_obj.house_name
  house_obj.house_price
  house_obj.house_location  


