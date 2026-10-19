day = input("What day is it? ").strip().lower()
time = input("What time of day (morning, afternoon, evening)? ").strip().lower()

if day == "monday" and time == "morning":
    print("Suggestion: Start the week off productive, learn some quantum computing!")
elif day == "monday" and time == "afternoon":
    print("Suggestion: Take a lunch break at the local Mozzarellita Pizza!")
elif day == "monday" and time == "evening":
    print("Suggestion: Wind down and make some herbal tea before bed")

elif day == "saturday" and time == "morning":
    print("Suggestion: You're never too old to watch some Saturday morning cartoons!")
elif day == "saturday" and time == "afternoon":
    print("Suggestion: Time for some brunch with the lads at Bill's Cafe!")
elif day == "saturday" and time == "evening":
    print("Suggestion: Saturday night means party time! Crack open a cold one!")

elif day == "sunday" and time == "morning":
    print("Suggestion: Sleep in bro it's sunday")
elif day == "sunday" and time == "afternoon":
    print("Suggestion: Eat some leftovers or something and go back to bed bud")
elif day == "sunday" and time == "evening":
    print("Suggestion: Time for a quick shower aaand back to bed you go")

elif day != "monday" and day != "saturday" and day != "sunday":
    print("Sorry, I don't recognize that day. Try: Monday, Saturday, Sunday...")
else:
    print("Sorry, I don't recognize that time. Try: Morning, Afternoon, Evening...")