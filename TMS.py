# print("Ticket Management System:")
# total_no_of_people =int(input("Enter number of passenger going to travel :-"))
# travel_km = int(input("Enter the travel KM :-"))
# print(f"Total no of tourist {total_no_of_people}")
# no_of_ticket_bus = 60
# bus_charge = 60
# print(f"Number of people a bus can accomodate {no_of_ticket_bus}")
# auto_people = 5
# auto_charge = 20
# print(f"Number of people a auto can accomodate {auto_people}")
# car_small_people = 3
# small_charge = 200
# print(f"Number of people a small car can accomodate {car_small_people}")
# car_big_people = 6
# big_cra_charge = 400
# print(f"Number of people a big car can accomodate {car_big_people}")
# bike_capcity = 2
# bike_charge = 7
# print(f"Number of people a bike can accomodate {bike_capcity}")


# charge_vehcil = {"BIKE": total_no_of_people * bike_charge * travel_km,
#                  "SMALL CAR":(total_no_of_people // car_small_people)*small_charge*travel_km,
#                  "BIG CAR": (total_no_of_people // car_big_people)*big_cra_charge*travel_km,
#                  "AUTO": ((total_no_of_people // auto_people)*auto_charge*travel_km),
#                  "BUS":total_no_of_people*bus_charge*travel_km
    
# }
# print(charge_vehcil)
# cheap =99999999999
# chaep_vehcil = ""
# Expensive = 0
# Expensive_veh = " "
# for i in charge_vehcil.keys() :
#     if(cheap > charge_vehcil[i]):
#         cheap = charge_vehcil[i]
#         chaep_vehcil = i
        
#     if(Expensive  < charge_vehcil[i]):
#         Expensive = charge_vehcil[i]
#         Expensive_veh = i

# print(f"The expensive vehcil is {Expensive_veh}. It's cost is {Expensive}")
# print(f"The cheapest vehcil is {chaep_vehcil}. It's cost is {cheap}")

# package1=["radharanitemple","janam bhoomi","bake bihari"]

# print("Ticket Management System")

# fares={}

# passgn_num=int(input("Enter Passenger Count : "))
# passgn_bus=60
# passgn_lrg_car=6
# passgn_sml_car=4
# passgn_auto=3
# passgn_bike=2
# trvl_km=40
# # per passenger
# fares['Bus']=60
# fares['Small_Car']=120
# fares['Large_Car']=150
# fares['Auto']=60
# fares['Bike']=40
# for i in fares:
#     print(f"Cost with {i} for {passgn_num} passengers is : {fares[i]*passgn_num}")

# max_cost = fares['Auto'] * passgn_num
# costliest_vehicle = 'Auto'
# for vehicle, fare in fares.items():
#     if fare * passgn_num > max_cost:
#         max_cost = fare * passgn_num
#         costliest_vehicle = vehicle
#     if fare * passgn_num < max_cost:
#         min_cost = fare * passgn_num
#         cheapest_vehicle = vehicle
# print(f"Costliest Vehicle is {costliest_vehicle} with Price:{max_cost}")
# print(f"Cheapest Vehicle is {cheapest_vehicle} with Price:{min_cost}")

print("Ticket Management System:-")
passgn_num=int(input("Enter Passenger Count:"))
tra_km= int(input("Enter kms to travel:"))
passgn_bus=60
passgn_lrg_car=6
passgn_sml_car=4
passgn_auto=3
passgn_bike=2
bus_charge=4
lrg_car_charge=150
small_car_charge=100
bike_charge=10
auto_charge=1
print("Number of buses needed:",passgn_num//passgn_bus+1)
print("Number of Large cars needed:",passgn_num//passgn_lrg_car+1)
print("Number of small cars needed",passgn_num//passgn_sml_car+1)
print("Number of auto needed:",passgn_num//passgn_auto+1)
print("Number of bike needed:",passgn_num//passgn_bike+1)
cost={
    "Cost of bus per person:":tra_km*passgn_bus,
    "Cost of small car per person:":tra_km*passgn_sml_car, 
    "Cost of auto per person:":tra_km*passgn_auto,
    "Cost of bike per person:":tra_km*passgn_bike,
    "Cost of large car per person:":tra_km*passgn_lrg_car                                              
}
print(cost)