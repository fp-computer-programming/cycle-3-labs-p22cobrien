# Author: CMOB 9/29/2021

total_points = input("how many points did the team score? ")

if int(total_points) <= 8:
    print("The team earned no medals.")
else:
    if int(total_points) <= 11:
        print("The team earned a bronze medal.")
    else:
        if int(total_points) < 15:
            print("The team earned a silver medal.")
        else:
            print("The team earned a gold medal.")
