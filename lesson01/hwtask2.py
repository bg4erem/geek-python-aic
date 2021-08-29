timeinsec = input("Input amount of seconds: ")

if not timeinsec.isdigit():
    print("Error, please type in number")
    exit()

timeinsec = int(timeinsec)

hours = timeinsec // 3600
minutes = (timeinsec % 3600) // 60
seconds = (timeinsec % 3600) % 60

print(f"Time is {hours:>02}:{minutes:>02}:{seconds:>02}")
