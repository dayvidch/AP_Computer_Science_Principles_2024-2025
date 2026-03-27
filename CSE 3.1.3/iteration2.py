x = input("what type of sandwich do you want? chicken $5.25, beef $6.25, tofu $5.75.")
print("your order is " + x)

if x.lower() == "chicken":
    s_price = 5.25
elif x.lower() == "beef":
    s_price = 6.25
elif x.lower() == "Tofu":
    s_price = 5.75
else:
    print("We do not have that")


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
    print("Answer in yes or no")

total_price = s_price + d_price
total_price_str = str(total_price)

print("Your total cost is $" + total_price_str)