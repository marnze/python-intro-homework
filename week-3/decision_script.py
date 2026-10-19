days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
energies = ["low", "medium", "high"]

while True:
    day = input("Enter what day it is today (e.g. Monday, Tuesday): ").strip().lower()
    if day in days:
        break
    print("Invalid day.")

while True:
    energy = input("Enter your energy level (Low, Medium, High): ").strip().lower()
    if energy in energies:
        break
    print("Invalid energy level.")

match (day, energy):
    case ("monday", "low"):
        print("You just got off a long work streak. Take it easy and rest up (after your workout)")
    case ("monday", "medium"):
        print("Finish up any CTD work before tomorrow's deadline.")
    case ("monday", "high"):
        print("Finish CTD work (if applicable), read up on tmrw's TIP101 session and finish at least 1 problem set")

    case ("tuesday", "low"):
        print("CTD Due Date tonight. Submit anything you have left and take the rest of the day off.")
    case ("tuesday", "medium"):
        print("CTD Due Date tonight. Submit what you have left and take a glance at tmrw's AI110 and WEB101 slides")
    case ("tuesday", "high"):
        print("CTD Due Date tonight. Submit what you have left, look at tmrw's AI110 and WEB101 slides and activities")

    case ("wednesday", "low"):
        print("Two classes in a row. Have the rest of the day off, you earned it (after your workout)")
    case ("wednesday", "medium"):
        print("Review any material you didn't quite grasp from today's classes for a bit and try to complete the activities")
    case ("wednesday", "high"):
        print("Review today's material if needed and finish any activities left over. Then take a peek at tmrw's TIP101 slides and complete at least 1 practice set")

    case ("thursday", "low"):
        print("Finished CodePath classes for the week. Take a breather for today")
    case ("thursday", "medium"):
        print("Review today's TIP101 material if needed and finish the problem set you were working on.")
    case ("thursday", "high"):
        print("Review today's material and finish the problem set. Also start looking at the new CTD week. 1 hr work is a plus")

    case ("friday", "low"):
        print("Friday fun day. Reach out to friends for some tennis or gaming (after your workout)")
    case ("friday", "medium"):
        print("Take the time to work on any projects due Sunday for CodePath. Also CTD week material")
    case ("friday", "high"):
        print("Work on CodePath projects due Sunday, finish CTD week material, and 1 hr work")

    case ("saturday", "low"):
        print("Take it easy today but try for 1 hr work")
    case ("saturday", "medium"):
        print("Continue working on any immediately due CodePath projects and finish CTD week material by today. Also 1 hr work")
    case ("saturday", "high"):
        print("CodePath projects work, CTD week finish by today, 2 hr work")

    case ("sunday", "low"):
        print("Last day for CodePath projects that are due. Finish them if applicable then complete 5 hr work and you're done")
    case ("sunday", "medium"):
        print("CodePath projects due tonight, 5 hr work done, start looking at next week CTD stuff")
    case ("sunday", "high"):
        print("CodePath projects due tonight, 5 hr work done, look at next week CTD stuff and TIP101 tuesday slides")