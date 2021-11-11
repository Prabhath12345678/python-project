Total_bill = input("what is the total bill?")
Percentage_tip = input("what percentage of tip is needed?")
Total_members = input("how many members is the bill split between?")

Total_bill = int(Total_bill)
Percentage_tip = int(Percentage_tip)
Percentage_tip = Percentage_tip/100
Total_members = int(Total_members)
#print(Percentage_tip)

Each_person_should_pay = (Percentage_tip*Total_bill+Total_bill)/Total_members
Final_amount = "{:.2f}".format(Each_person_should_pay)
print(f"Each person should pay {Final_amount}")
