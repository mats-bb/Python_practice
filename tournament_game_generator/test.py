my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Calculate the number of pairs
for i in range(len(my_list) // 2):
        away = my_list[i]
        home = my_list[-(i + 1)]
        print(f"Home: {home} VS Away: {away}")