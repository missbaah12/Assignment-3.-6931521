# list of available cars and their prices at Erata Motors
cars = {
'Toyota Landcruiser' : 657585,
'Toyota Corolla' : 40000,
'Toyota Rav4': 894948,
'Toyota Prado' : 647788,
'Hyundai Elantra' : 4000000,
'Hyundai Tucson' : 38927376,
'Hyundai Accent' : 8474649,
'Acura' : 6000000,
'Lamborghini Aventador' : 800000,
'Lamborghini Urus' : 70000,
'Tesla Cybertruck' : 5900000,
'Tesla Model S' : 3788373,
'Tesla Model Y' : 2387747,
'Tesla model 3' : 443800,
'Bugatti Chiron' : 886478,
'Bugatti Divo' : 5474746,
'Saturn' : 94876464,
'Jeep Wrangler' : 65736363,
'Jeep Compass' : 69363636,
'Jeep Grand Cherokee' : 57273366,
'Ferrari 250 GTO' : 683939,
'Ferrari 599 GTO' : 400000,
'Chevrolet Cruze' : 63738899,
'Chevrolet Equinox' : 28736367,
'Chevrolet Camaro' : 8394947,
'Kia' : 93847646,
'Lexus Lx570' : 7585859,
'Lexus Gx 460' : 849494,
'BMW 4 series convertible' : 748494667,
'BMW 5 series sedan' : 54200000,
'Mazda 3' : 9393837,
'Mazda 6' : 3938375,
'Ford Focus' : 5783633,
'Ford Explorer' : 3737358,
'Ford Escape' : 3663738,
'Audi' : 8364889,
'Mitsubishi' : 700000,
'Volvo' : 8474669,
'Honda' : 5000000,
'Bentley' :58474679,
'Maserati' : 80000090,
'Jaguar' : 7484948,
'Land rover' : 83737478,
'Range rover evoque' : 21830000,
'Rolls-Royce phantom' : 5980000,
'Infiniti' : 648484679,
'Aston Martin' : 90000
}  
carName = input("Enter Your Preferred Car's Name': ")
if carName in cars:
    print("Yes Your Car is Available")
    carPrice = cars[carName]
    print(f"The price of {carName} is ${carPrice}.")
else:   
    print(f"Sorry,{carName} is not available")
#GitHub repository: https://github.com/missbaah12

