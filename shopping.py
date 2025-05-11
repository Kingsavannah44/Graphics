cars = ["bmw", "audi", "mercedes", "tesla"]
print(cars)
X=cars[0]
print (X)
cars[0]="ford"
print(cars)cars = ["bmw", "audi", "mercedes", "tesla"]
print("Original List:", cars)
first_car = cars[0]
print("First Car:", first_car)
cars[0] = "ford"
print("Updated List:", cars)
for car in cars:
    print("Car:", car)
cars.append("toyota")
print("Updated List after append:", cars)
for x in cars:
    print(x)
cars.append("toyota")
print(cars)