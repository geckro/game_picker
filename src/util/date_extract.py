# Extracts date from column 2 of csv document
def date_extraction(date_str):
# Extract year, month, and day from date string
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:8]

    # Format date as yyyy-mm-dd (2022-05-27)
    date_str = f"{year}-{month}-{day}"
    
    # return the formatted date_str
    return date_str