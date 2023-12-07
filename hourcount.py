# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"


hour_counts = dict()

with open(name, 'r') as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if len(words) >= 6:
                time = words[5]
                hour = time.split(':')[0]
                hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Using tuples to store hour-count pairs and sorting them by hour
hour_tuples = sorted(hour_counts.items())

# Printing the counts sorted by hour
for hour, count in hour_tuples:
    print(hour, count)
