import os
def customcsv():
    csv = "data/custom.csv"
    if not os.path.isfile(csv):
        # create the file
        with open(csv, "w") as f:
            # write some initial data to the file if needed
            f.write("some initial data\n")
        return f"{csv} created successfully!"
    else:
        return f"{csv} already exists!"

def owned_games():
    csv = customcsv()
    print(csv)