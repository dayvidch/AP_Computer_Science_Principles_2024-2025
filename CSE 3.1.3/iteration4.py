x = input("what type of sandwich do you want? chicken $5.25, beef $6.25, tofu $5.75.")
print("your order is " + x)

if x.lower() == "chicken":
    s_price = 5.25
    sand_bought = True
elif x.lower() == "beef":
    s_price = 6.25
    sand_bought = True
elif x.lower() == "tofu":
    s_price = 5.75
    sand_bought = True
else:
    print("We do not have that, please start over")
    exit()
    


y = input("Would you like a drink? Answer in yes or no. ")
if y.lower() == "yes":
    z = input("What size drink would you like? small $1.00, medium $1.75, large $2.25 ")

    if z == "small":
        d_price = 1.00
        drink_bought = True
    elif z == "medium":
        d_price = 1.75
        drink_bought = True
    else:
        d_price= 2.25
        drink_bought = True

elif y.lower() == "no":
        print("no drinks")
        d_price = 0
        drink_bought = False

else:
    print("Answer in yes or no, please restart")
    exit()


total_price = s_price + d_price
total_price_str = str(total_price)

#print("Your total cost is $" + total_price_str)



fries = {"small": 1.00, "medium": 1.50, "large": 2.00}

fries_choice = input("Would you like to get some fries? Answer in yes or no.")
if fries_choice.lower() == "yes":
    size_choice = input("What size of fries would you like? Small : $1.00, Medium : $1.50, Large: $2.00 ")
    if size_choice.lower() == "small":
        fries_bought = True
        mega_choice = input("Would you like to mega-size your fries? Yes or No.")
        if mega_choice.lower() == "yes":
            fries_cost = fries.get("large")
            fries_bought = True
            size_choice = "Jumbo"
        else:
            fries_cost = fries.get("small")
            fries_bought = True
    elif size_choice.lower() == "medium":
        fries_cost = fries.get("medium")
        fries_bought = True
    elif size_choice.lower() == "large":
        fries_bought = True
        fries_cost = fries.get("large")
else:
    size_choice = "No Fries"
    fries_cost = 0
    fries_bought = False

part3_total = total_price + fries_cost
part3_total_str = str(part3_total)

print("Your fries selection was "+ size_choice)

#print("Your total is $ " + part3_total_str)



ketchup = input("Would you like any ketchup packets? Yes or No. ")
if ketchup.lower() == "yes":
    numKetchup = input("How many? in numbers. ")
    ketchup_bought = True
    ketchup_total = int(numKetchup) * 0.25
else:
    numKetchup = "NO"
    ketchup_bought = False
ketchup_total = 0

#final_order_before_reduction = m

if sand_bought and drink_bought and fries_bought == True:
    reduced_price = part3_total - 1.00
    final_price = str(reduced_price)
else:
    final_price = part3_total_str

print("Your final order is " + str(x.upper()) +  " SANDWICH, " + str(z.upper()) + " DRINK, " + str(size_choice.upper()) + " FRIES, " + str(numKetchup) + " KETCHUP PACKETS")
print("Your final cost is $" + str(final_price))

