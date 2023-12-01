n = 5
counter = 0
# collect counter in a list
counter_list = []

while counter < n:
    counter += 1
    # add count to counter list
    counter_list.append(counter)

# sum all counter in the counter list and display total
print(sum(counter_list))
