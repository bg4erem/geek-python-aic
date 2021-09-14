from sys import argv

try:
    check, hours, hour_rate, prem = argv
except ValueError:
    print("Arguments error")

hours = int(hours)
hour_rate = int(hour_rate)
prem = int(prem)

def salary(hours, hour_rate, prem):
    print(f"Salary according to your parameters: {prem + (hours*hour_rate)}")
    print(f"Details of the calculation: worked hours {hours} * hour rate {hour_rate} + premium {prem}")
salary(hours,hour_rate, prem)

