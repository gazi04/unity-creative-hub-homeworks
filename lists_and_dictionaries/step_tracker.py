days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [8200, 12500, 6400, 10100, 11800, 15300, 4700]
goal = 10000

goal_steps = []
goal_days = []
streak = 0
best_streak = 0
status = "Needs more walking"

print("===== WEEKLY STEPS =====")
for i in range(len(steps)):
    if steps[i] >= goal:
        print(f"{days[i]}: {steps[i]} steps - Goal reached")
        goal_steps.append(steps[i])
        goal_days.append(days[i])
        streak += 1
        best_streak = max(streak, best_streak)
    else:
        print(f"{days[i]}: {steps[i]} steps - Missed")
        streak = 0

total_steps = sum(goal_steps)
avg = total_steps / len(goal_steps)

best_score = max(steps)
worst_score = max(steps)

best_day = days[steps.index(best_score)]
worst_day = days[steps.index(worst_score)]

if avg > 10000:
    status = "Very active"
elif avg > 7500:
    status = "Active"

print("------------------------")
print("Total Steps:", total_steps)
print("Average Steps:", avg)

print(f"Best Day: {best_day} ({best_score})")
print(f"Worst Day: {worst_day} ({worst_score})")

print("Goal Days:", goal_days)
print(f"Goal Reached: {len(goal_days)}/{len(days)} days")
print(f"Longest Streak: {best_streak} days")


print("Status:", status)
print("========================")
