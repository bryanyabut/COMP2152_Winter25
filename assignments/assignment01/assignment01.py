'''
AUTHOR: BRYAN PAUL YABUT
ASSIGNMENT 1
'''

gym_member = "Alex Milton" # GYM MEMBER

preferred_weight = 20.5 # PREFERRED WEIGHT IN KG

highest_reps = 25 # HIGHEST REPITIONS

membership_active = True # MEMBERSHIP STATUS ACTIVE

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (10, 50, 35),
    "Taylor": (5, 32, 21)
}

# total_workout = tuple(sum(x) for x in zip(*workout_stats.values())) # TOTAL WORKOUT
# # temp =[]
# # for x in workout_stats.values():
# #     temp.append(list(x))
# #     total_workout = tuple(map(sum, temp))

# for key, value in workout_stats.values():
#     workout_stats(name = "total_of ") = workout_stats(key)
#     print("name each person is: " + str(total_workout))
# dictionary to
totals = {name: sum(times) for name, times in workout_stats.items()}

for name, total in totals.items():
    print(f"{name}: {total} minutes")