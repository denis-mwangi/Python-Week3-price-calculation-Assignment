# Question 1
def calculateDiscount(price, discountPercent):
    discount = discountPercent/100
    if discount >= 0.2:
        finalPrice = price - price*discount
    else:
        finalPrice = price
    return finalPrice

# Question 2
price = int(input("Enter the price: "))
discountPercent = int(input("Enter the discount percentage: "))
finalPrice = calculateDiscount(price, discountPercent)
print(f"The final price is {finalPrice}")