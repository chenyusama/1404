from prac_09.unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("Aido", 100, 90)

    print(f"{car.name} drove {car.drive(150):2}km.")

main()