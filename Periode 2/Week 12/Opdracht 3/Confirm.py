def confirm(message):
    response = input(f"{message} (yes/no): ").strip().lower()
    return response in ["yes", "y"]

if confirm("Do you like pizza?"):
    print("User confirmed")
else:
    print("User canceled")
