# Team Members: [Nicol Aidan]
# Course: CS151, Dr. Rajeev
# Programming Assignment: 6
# Program Inputs: [file]
# Program Outputs: [difference in deaths to a file, graphs, avg, amount of damage to crops by storm]

import matplotlib.pyplot as plt
#
startYearMonth = 0
# 0. The year and month in the format YYYYMM in which the storm started

startDay = 1
# 1. The day of the month in which the storm started

startTime = 2
# 2. The time at which the storm started

endYearMonth = 3
# 3. The year and month in the format YYYYMM in which the storm ended

endDay = 4
# 4. The day of the month in which the storm ended

endTime = 5
# 5. The time at which the storm ended

stormState = 6
# 6. The name of the state where storm occurred

stormType = 7
# 7. The type of storm

stormDirectInjuries = 8
# 8. The number of injuries directly caused by the storm

stormIndirectInjuries = 9
# 9. The number of injuries indirectly caused by the storm

stormDirectDeaths = 10
# 10. The number of deaths directly caused by the storm

stormIndirectDeaths = 11
# 11. The number of deaths indirectly caused by the storm

damageProperty = 12
# 12. The amount of damage to property

damageCrops = 13
# 13. The amount of damage to crops


def read_file(file_name):
    all_data = []

    #open file named filename for reading

    try:
        file = open(file_name, "r")

        for line in file:
            #it loops through all the lines and the files that we just opened
            temp=line.split(",")
            #temp is now a list separated
            all_data.append(temp)
            #add a list to the overall list


        file.close()
    except FileNotFoundError:
        print("File not found")

    return all_data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def difference(all_data):
    output = open(input("Enter file name to output data to: "), "w")
    for line in all_data:
        # difference and absolute values
        diff = int((line[stormDirectDeaths]) - (line[stormDirectInjuries]))
        # checking difference
        if diff <= -5:
            sig = "significantly fewer deaths than injuries"
        elif diff > -5 and diff < -1:
            sig = "fewer deaths than injuries"
        elif diff >= -1 and diff <= 1:
            sig = "no significant change to deaths and injuries"
        elif diff > 1 and diff < 5:
            sig = "more deaths than injuries"
        else:
            sig = "significantly more deaths than injuries"
    # writes new file
    output.write(str(diff) + " = " + str(sig) + "\n")

# this is the difference function
# What is the difference in deaths and injuries directly caused by each storm?
# Were there significant fewer, fewer, the same, more, or significantly more injuries than deaths?
# You should consider a change of +/- 1 to be no change. Changes for +/- 5 are significant.
# This information should be output for each storm to a file that the user chooses.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def storm_graph(all_data):
    # dictionary
    property_damage = {'none': 0, 'low': 0, 'moderate': 0, 'high': 0}
    # checks matches
    for line in all_data:
        dmg = line[damageProperty]
        if dmg == 0:
            property_damage['none'] += 1
        elif dmg < 1000:
            property_damage['low'] += 1
        elif dmg < 10000:
            property_damage['moderate'] += 1
        else:
            property_damage['high'] += 1

    # graph
    key = list(property_damage.keys())
    value = list(property_damage.values())
    colors = ['r', 'y', 'g', 'b']
    plt.bar(value, labels = key, color = colors, width = 0.5)
    plt.title("Property Damage Graph")
    plt.xlabel("Level of Damage")
    plt.ylabel("Storms")
    plt.show()

# this is the graph  function
# Create a graph that shows the number of storms with no, low, moderate moderate, and high damage to property.
# Low damage is less than 1000 and high damage is greater than 10000.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def damaged_crops(all_data):
    crops = {}
    #
    for line in all_data:
        type = line[stormType]
        temp = line[damageCrops]
        if temp > 0 and type not in crops:
            crops[type] = float(temp)
        else:
            crops[type].extend(float(temp))
    #
    for key in crops:
        print(key + ": " + crops.values())

# this is the damage function
# create a function that says what type of storm damaged crops
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def avg_days(all_data):
    storm_avg = {}
    for line in all_data:
        # type of storm and days (plus one is to include starting day)
        type = line[stormType]
        time = line[endDay] - line[startDay] + 1
        # checking if type has been added to dictionary
        if type not in storm_avg:
            storm_avg[type] = int(time)
        else:
            storm_avg[type].extend(int(time))
    # finding average
    for key in storm_avg:
        print(key + " days".format(storm_avg[key])/len(storm_avg[key]))

# this is for the avg
# What was the average number of days that each type of storm lasted?
# You can ignore the time of day and only look at the date. But be careful --
# if it starts and ends on teh same day, it counts as lasting for 1 day, not zero.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def main():
    # read in the file
    all_data = read_file("storm2000.csv")
    while all_data == []:
        # menu
        print("Please pick one from the following options")

        print("Option a: Difference of Direct Deaths & Injuries")

        print("Option b: Graphs Storms")

        print("Option c: Average Days")

        print("Option d: Damage to Crop by Storm")

        print("Option e: I'm done")
        option = input("Please enter which option you want: ")
        option.strip().lower()
        while option != "a" and option != "b" and option != "c" and option != "d" and option != "e":
            print("Please enter a valid option, try again")
            print("Please pick one from the following options")
            print("Option a: Difference of Deaths")

            print("Option b: Graphs Storms")

            print("Option c: Average Days")

            print("Option d: Damage to Crop by Storm")

            print("Option e: I'm done")
            option = input("Please enter which option you want: ")
            option.strip().lower()
        if option == "a":
            # calls different function
            difference(all_data)
        elif option == "b":
            # call the graph function
            storm_graph(all_data)
        elif option == "c":
            # call the avg date
            avg_days(all_data)
        elif option == "d":
            # call the damage caused
            damaged_crops(all_data)
        elif option == "e":
            # ends program
            break
        else:
            continue


main()