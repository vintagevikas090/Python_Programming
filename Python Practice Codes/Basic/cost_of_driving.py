# Problem Statement:
#     Assume you travel 80 km to and fro in a day. 
#     Cost of Diesel per litre is 80 INR 
#     Your vehicle Fuel Average is 18 km/litre. 
#     Now calculate the cost of driving per day to office. 

dist = int(input("Enter the distance: "))
avg = int(input("Average of vehicle: "))
d_cost = int(input("Diesel cost: "))
fuel_req = dist/avg
total_cost = fuel_req*d_cost
print("Total cost for the given distance is ", total_cost)
