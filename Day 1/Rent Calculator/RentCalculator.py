## Input we need from the User
## Total Rent 
## Total Food Ordered From SnaKing
## Electricity Unit Spends 
## Charge per unit
## Persons Living in room/flat 

## Output 
# Total amount you've to pay is 

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend  = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter The Charge Per Unit = "))
person = int(input("Enter the number of person living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = rent + food + total_bill / person

print("Each Person Will pay ", output)