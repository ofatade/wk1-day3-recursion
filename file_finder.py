def find_target(file_system, target):

    for item in file_system:

        if isinstance(item, str):  # Check if item is a file (string)

            if item == target:
                print("big HOORAY")
                return True  # Stop searching once the target is found
            
        elif isinstance(item, list):  # Check if item is a folder (list)

            if find_target(item, target):  # Recursively search in the subfolder
                return True
            
    return False  # Return False if the target is not found in this path

# CODE TEST
file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

find_target(file_system, target) # This will print "big HOORAY"

find_target(file_system, "darezy_file.txt") # This will print NOTHING