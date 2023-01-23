from prac_09.silver_service_taxi import SilverServiceTaxi

better_taxi = SilverServiceTaxi(100, "Sliver service", 2)
print(better_taxi.price_per_km)
better_taxi.drive(18)
print(better_taxi.get_fare())
print(better_taxi)