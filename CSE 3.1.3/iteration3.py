x = input("what type of sandwich do you want? chicken $5.25, beef $6.25, tofu $5.75.")
print("your order is " + x)

if x.lower() == "chicken":
    s_price = 5.25
elif x.lower() == "beef":
    s_price = 6.25
elif x.lower() == "tofu":
    s_price = 5.75
else:
    print("We do not have that, please start over")
    exit()


y = input("Would you like a drink? Answer in yes or no. ")
if y.lower() == "yes":
    z = input("What size drink would you like? small $1.00, medium $1.75, large $2.25 ")

    if z == "small":
        d_price = 1.00
    elif z == "medium":
        d_price = 1.75
    else:
        d_price= 2.25

elif y.lower() == "no":
    print("no drinks")
    d_price = 0

else:
    print("Answer in yes or no, please restart")
    exit()


total_price = s_price + d_price
total_price_str = str(total_price)

print("Your total cost is $" + total_price_str)



fries = {"small": 1.00, "medium": 1.50, "large": 2.00}

fries_choice = input("Would you like to get some fries? Answer in yes or no.")
if fries_choice.lower() == "yes":
    size_choice = input("What size of fries would you like? Small : $1.00, Medium : $1.50, Large: $2.00 ")
    if size_choice.lower() == "small":
        mega_choice = input("Would you like to mega-size your fries? Yes or No.")
        if mega_choice.lower() == "yes":
            fries_cost = fries.get("large")
            size_choice = "Jumbo"
        else:
            fries_cost = fries.get("small")
    elif size_choice.lower() == "medium":
        fries_cost = fries.get("medium")
    elif size_choice.lower() == "large":
        fries_cost = fries.get("large")
else:
    fries_cost = 0

part3_total = total_price + fries_cost
part3_total_str = str(part3_total)

print("Your fries selection was "+ size_choice)

print("Your total is $ " + part3_total_str)