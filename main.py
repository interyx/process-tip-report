import sys
import pandas
from datetime import datetime
from collections import namedtuple

def main():
    filepath = "invalid"
    if sys.argv[1:]:
        filepath = sys.argv[1]
    if filepath == "invalid":
        print("invalid filename")
        sys.exit()
    items = []
    with open(filepath) as f:
        data = f.readlines()
    processed_data = []
    for datum in data:
        processed_data.append(datum.rstrip())
    try:
        while processed_data:
            store = processed_data.pop(0)
            name = processed_data.pop(0)
            number = processed_data.pop(0)
            hours = processed_data.pop(0)
            items.append({"Store": store, "Name": name, "Number": number, "Hours": hours})
    except IndexError:
        print("Index error occurred.  Is your data misshapen?")
    df = pandas.DataFrame(items)
    df.drop(columns=['Store', 'Number'], inplace=True)
    current_date = datetime.now()
    output = f"./{current_date.year}.{current_date.month}.{current_date.day}.csv"
    df.to_csv(output, index=False)
    print(f"{filepath} converted successfully!  Output stored in {output}.")


if __name__ == "__main__":
    main()