# Extracts date from column 2 of csv document
def date_extraction(date_str):
    # first 4 characters
    year = date_str[:4]
    # character 5 and 6
    month = date_str[4:6]
    # character 7 and 8
    day = date_str[6:8]

    date_str = f"{year}-{month}-{day}"
    if date_str.endswith("-"):
                date_str = date_str[:-1]
                if date_str.endswith("-"):
                    date_str = "no-date"
    return date_str