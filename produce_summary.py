def print_summary(day_num, file_name):
    """From day and text file, prints a summary of deliveries
    
    Opens file, splits line, assigns variable to each substring, inserts
    into a print statement"""

    print("Day:", day_num)
    
    # open file and set to variable
    deliveries = open(file_name)

    # empty variable for days earnings
    total_earnings = 0

    # iterate over each line from file
    for delivery in deliveries:
        delivery = delivery.rstrip()  # strip trailing whitespace
        delivery_info = delivery.split("|")  # create list of substrings

        # assign each item to  variable
        melon = delivery_info[0]
        melon_count = delivery_info[1]
        price = delivery_info[2]

        # from solution: also melon, melon_count, price = delivery_info

        # turn price str to float and add to total
        total_earnings += float(price)

        # display info for each delivery
        print(f"Delivered {melon_count} {melon}s for total of ${price}")

    # display total of prices from day
    print(f"Day {day_num} earnings = ${total_earnings}")
    print()
    deliveries.close() 

# call function for each report
print_summary(1, "um-deliveries-day-1.txt")
print_summary(2, "um-deliveries-day-2.txt")
print_summary(3, "um-deliveries-day-3.txt")
