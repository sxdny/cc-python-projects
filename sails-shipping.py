weight = 2 # lb
gs_price = 0
ds_price = 0
pr_ground_shipping_cost = 125.00

# Ground Shipping
print("Ground Shipping plan:")
if weight <= 2:
  print("1.50$ per pound + 20$ of flat charge.")
  price = str(1.50 * weight + 20)
  print("The price of shipping is: $" + price)
  gs_price = float(price)
elif weight > 2 and weight <= 6:
  print("3.00$ per pound + 20$ of flat charge.")
  price = str(3.00 * weight + 20)
  print("The price of shipping is: $" + price)
  gs_price = float(price)
elif weight > 6 and weight <= 10:
  print("4.00$ per pound + 20$ of flat charge.")
  price = str(4.00 * weight + 20)
  print("The price of shipping is: $" + price)
  gs_price = float(price)
else:
  print("4.75$ per pound + 20$ of flat charge.")
  price = str(4.75 * weight + 20)
  print("The price of shipping is: $" + price)
  gs_price = float(price)

print("\n")
print("Premium Ground Shipping Cost: $" + str(pr_ground_shipping_cost))
print("\n")

# Drone Shipping
print("Drone Shipping plan:")
if weight <= 2:
  print("4.50$ per pound + 0$ of flat charge.")
  price = str(4.50 * weight)
  print("The price of shipping is: $" + price)
  ds_price =float(price)
elif weight > 2 and weight <= 6:
  print("9.00$ per pound + 0$ of flat charge.")
  price = str(9.00 * weight)
  print("The price of shipping is: $" + price)
  ds_price = float(price)
elif weight > 6 and weight <= 10:
  print("12.00$ per pound + 0$ of flat charge.")
  price = str(12.00 * weight)
  print("The price of shipping is: $" + price)
  ds_price = float(price)
else:
  print("14.25$ per pound + 0$ of flat charge.")
  price = str(14.25 * weight)
  print("The price of shipping is: $" + price)
  ds_price = float(price)

# Best option
print("\n")
print("Price with Ground Shipping: $" + str(gs_price))
print("Price with Premium Ground Shipping: $" + str(pr_ground_shipping_cost))
print("Price with Drone Shipping: $" + str(ds_price))

# Find the best option
prices = [gs_price, pr_ground_shipping_cost, ds_price]
best_plan = 0

print("\n")
for i, x in enumerate(prices):
  ipac = i
  for y, x in enumerate(prices):
    if prices[ipac] < prices[y] and prices[ipac] < prices[best_plan]:
      best_plan = ipac

# print the best plan
if best_plan == 0:
  print("The best plan for you is: Ground Shipping Plan")
elif best_plan == 1:
  print("The best plan for you is: Premium Ground Shipping Plan")
else:
  print("The best plan for you is: Drone Shipping Plan")