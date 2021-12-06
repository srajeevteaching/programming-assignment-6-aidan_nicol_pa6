# Team Members: [Nicol Aidan]
# Course: CS151, Dr. Rajeev
# Programming Assignment: 6
# Program Inputs: [file]
# Program Outputs: [difference in deaths to a file, graphs, avg, amount of damage to crops by storm]

# The year and month in the format YYYYMM in which the storm started
# The day of the month in which the storm started
# The time at which the storm started
# The year and month in the format YYYYMM in which the storm ended
# The day of the month in which the storm ended
# The time at which the storm ended
# The name of the state where storm occurred
# The type of storm
# The number of injuries directly caused by the storm
# The number of injuries indirectly caused by the storm
# The number of deaths directly caused by the storm
# The number of deaths indirectly caused by the storm
# The amount of damage to property
# The amount of damage to crops

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
    except:
        print("File not found")

    return all_data

# this is the difference function
# What is the difference in deaths and injuries directly caused by each storm?
# Were there significant fewer, fewer, the same, more, or significantly more injuries than deaths?
# You should consider a change of +/- 1 to be no change. Changes for +/- 5 are significant.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# this is the graph  function
# Create a graph that shows the number of storms with no, low, moderate moderate, and high damage to property.
# Low damage is less than 1000 and high damage is greater than 10000.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# this is the damage function
# create a function that compares the damage to cro by the type
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# this is for the avg
# What was the average number of days that each type of storm lasted?
# You can ignore the time of day and only look at the date. But be careful --
# if it starts and ends on teh same day, it counts as lasting for 1 day, not zero.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def main():
    # read in the file
    user_file = input("Please enter the name of the file: ")
    all_data = read_file(user_file)
    while all_data == []:
        user_file = input("Please enter the name of the file: ")
        all_data = read_file(user_file)


    # menu

        print("PLease pick one from the following options")

        print("Option a: Difference od deaths")

        print("Option b: graphs storms")

        print("Option c: avg days lasted")

        print("Option d: damage to crop by storm")

        print("Option e: I'm done")
        option = input("Please enter which option you want: ")
        option.strip().lower()
        while option != "a" and option != "b" and option != "c" and option != "d" and option != "e":
            print("Please enter a valid option, try again")
            print("Please pick one from the following options")
            print("Option a: Difference od deaths")

            print("Option b: graphs storms")

            print("Option c: avg days lasted")

            print("Option d: damage to crop by storm")

            print("Option e: I'm done")
            option = input("Please enter which option you want: ")
            option.strip().lower()
        if option == "a":
    # calls different function
    # call the graph function
    # call the avg date
    # call the damage caused
    # end the program


