print("welcome to tio calcultor")
#Take input form user
bill =float(input("Entrt bill\n"))
tip = int(input("How much tip you want to give ig, 10,20...!plse don't add %\n"))
splt = int(input("how many people to splt the bill:\n "))
# Calculate the tip
tip_as_per = tip/100
# Total tip ammount
tip_am = bill*tip_as_per
#Total bil ammount
total_bill_amount = bill+tip_am
#split the bill with pepole
split_bill = total_bill_amount / splt
#2 round of the bill using round  fuction.
final_amount= round(split_bill,2)
#the final bill print.
print(f"each person should pay:{final_amount}")
 
