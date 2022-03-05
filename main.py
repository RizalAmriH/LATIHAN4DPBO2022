from job import job
from plane import plane
from ship import ship
from driver import driver

#inisisasi object
plane1 = plane(10 , "tempur", 200)
plane1.set_fuelType("Avtur")
plane1.set_maxPassenger(6)

plane2 = plane(2,"jet", 100)
plane2.set_fuelType("Avtur")
plane2.set_maxPassenger(20)

plane3 = plane(5, "penumpang ukuran sedang", 120)
plane3.set_fuelType("Avtur")
plane3.set_maxPassenger(200)

plane4 = plane(8, "kargo", 300)
plane4.set_fuelType("Avtur")
plane4.set_maxPassenger(10)

plane5 = plane(3, "penumpang ukuran besar", 300)
plane5.set_fuelType("Avtur")
plane5.set_maxPassenger(350)


ship1 = ship(4,"Boat", "USA")
ship1.set_fuelType("Solar")
ship1.set_maxPassenger(8)

ship2 = ship(2,"Ferry", "Rusia")
ship2.set_fuelType("Solar")
ship2.set_maxPassenger(80)

ship3 = ship(4,"Boat", "USA")
ship3.set_fuelType("Solar")
ship3.set_maxPassenger(8)

ship4 = ship(6,"Cargo", "UK")
ship4.set_fuelType("Solar")
ship4.set_maxPassenger(18)

ship5 = ship(10,"SubMarine", "Netherland")
ship5.set_fuelType("Solar")
ship5.set_maxPassenger(30)

job1 = job(112131314, "Facebook", "UX Reseacrher")
job1.set_NIK(1000000)
job1.set_name("Abdul Rahman")
job1.set_gender("Male")

job2 = job(12131411, "Instagram", "Mobile App Engineer")
job2.set_NIK(1425252)
job2.set_name("Rizal Amri")
job2.set_gender("Male")

job3 = job(888877, "Ajinomoto", "Manager")
job3.set_NIK(1211141)
job3.set_name("Ruby")
job3.set_gender("Female")

job4 = job(155111, "Google", "Data Analist")
job4.set_NIK(1022420)
job4.set_name("Stevenson Utomo")
job4.set_gender("Male")

job5 = job(311141515, "Jaya Sentosa", "CEO")
job5.set_NIK(13154372)
job5.set_name("Budi Subagja")
job5.set_gender("Male")



driver1 = driver(132524, 2023, "Car")
driver1.set_NIK(2131414)
driver1.set_name("Rudi Khoerudin")
driver1.set_gender("Male")

driver2 = driver(222222, 2025, "Car")
driver2.set_NIK(324241)
driver2.set_name("Radit Venn")
driver2.set_gender("Male")

driver3 = driver(4244171, 2023, "Motobike")
driver3.set_NIK(213131)
driver3.set_name("Bambang")
driver3.set_gender("Male")

driver4 = driver(333334, 2025, "Motobike")
driver4.set_NIK(145411)
driver4.set_name("Angelina")
driver4.set_gender("Female")

driver5 = driver(797975, 2024, "Truck")
driver5.set_NIK(999997)
driver5.set_name("Suripto")
driver5.set_gender("Male")


#print data

print("===== AIRPLANE =====")
plane1.print_info()
print("FUELTYPE = " + str(plane1.get_fuelType()))
print("MAX PASSENGER = " + str(plane1.get_maxPassenger()))
print("---------------")
plane2.print_info()
print("FUELTYPE = " + str(plane2.get_fuelType()))
print("MAX PASSENGER = " + str(plane2.get_maxPassenger()))
print("---------------")
plane3.print_info()
print("FUELTYPE = " + str(plane3.get_fuelType()))
print("MAX PASSENGER = " + str(plane3.get_maxPassenger()))
print("---------------")
plane4.print_info()
print("FUELTYPE = " + str(plane4.get_fuelType()))
print("MAX PASSENGER = " + str(plane4.get_maxPassenger()))
print("---------------")
plane5.print_info()
print("FUELTYPE = " + str(plane5.get_fuelType()))
print("MAX PASSENGER = " + str(plane5.get_maxPassenger()))
print("---------------")

print("===== SHIP =====")
ship1.print_info()
print("FUELTYPE = " + str(ship1.get_fuelType()))
print("MAX PASSENGER = " + str(ship1.get_maxPassenger()))
print("---------------")
ship2.print_info()
print("FUELTYPE = " + str(ship2.get_fuelType()))
print("MAX PASSENGER = " + str(ship2.get_maxPassenger()))
print("---------------")
ship3.print_info()
print("FUELTYPE = " + str(ship3.get_fuelType()))
print("MAX PASSENGER = " + str(ship3.get_maxPassenger()))
print("---------------")
ship4.print_info()
print("FUELTYPE = " + str(ship4.get_fuelType()))
print("MAX PASSENGER = " + str(ship4.get_maxPassenger()))
print("---------------")
ship5.print_info()
print("FUELTYPE = " + str(ship5.get_fuelType()))
print("MAX PASSENGER = " + str(ship5.get_maxPassenger()))
print("---------------")

print("===== JOB =====")
job1.print_info()
print("NAME = " + str(job1.get_name()))
print("NIK = " + str(job1.get_NIK()))
print("GENDER = " + str(job1.get_gender()))
print("---------------")
job2.print_info()
print("NAME = " + str(job2.get_name()))
print("NIK = " + str(job2.get_NIK()))
print("GENDER = " + str(job2.get_gender()))
print("---------------")
job3.print_info()
print("NAME = " + str(job3.get_name()))
print("NIK = " + str(job3.get_NIK()))
print("GENDER = " + str(job3.get_gender()))
print("---------------")
job4.print_info()
print("NAME = " + str(job4.get_name()))
print("NIK = " + str(job4.get_NIK()))
print("GENDER = " + str(job4.get_gender()))
print("---------------")
job5.print_info()
print("NAME = " + str(job5.get_name()))
print("NIK = " + str(job5.get_NIK()))
print("GENDER = " + str(job5.get_gender()))
print("---------------")

print("===== DRIVER =====")
driver1.print_info()
print("NAME = " + str(driver1.get_name()))
print("NIK = " + str(driver1.get_NIK()))
print("GENDER = " + str(driver1.get_gender()))
print("---------------")

driver2.print_info()
print("NAME = " + str(driver2.get_name()))
print("NIK = " + str(driver2.get_NIK()))
print("GENDER = " + str(driver2.get_gender()))
print("---------------")

driver3.print_info()
print("NAME = " + str(driver3.get_name()))
print("NIK = " + str(driver3.get_NIK()))
print("GENDER = " + str(driver3.get_gender()))
print("---------------")

driver4.print_info()
print("NAME = " + str(driver4.get_name()))
print("NIK = " + str(driver4.get_NIK()))
print("GENDER = " + str(driver4.get_gender()))
print("---------------")

driver5.print_info()
print("NAME = " + str(driver5.get_name()))
print("NIK = " + str(driver5.get_NIK()))
print("GENDER = " + str(driver5.get_gender()))

