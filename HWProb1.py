quantity = int(input("Enter the quantity: "))

if quantity >= 1000:
    unit_price = 3.00
else:
   unit_price = 5.00
  
extended_price = quantity * unit_price

tax = extended_price * 0.07

total = extended_price + tax

print(f"{quantity:<12}{unit_price:>12.2f}{extended_price:>18.2f}{tax:>12.2f}{total:>12.2f}")
