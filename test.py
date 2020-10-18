"""Data analysis file for Covid_Data_Bot"""

from typing import Dict, List 
from csv import DictReader

READ_MODE = "r"
file_path = "Covid_Data.csv"





def loop_and_create(file_path: str) -> List[Dict[str, str]]:

    """Opens a csv file and simplifies the data."""
    file_handle = open(file_path, READ_MODE, encoding="utf8")
    csv_reader = DictReader(file_handle)
    table: List[Dict[str, str]] = []

    for row in csv_reader:
        str_row: Dict[str, str] = {}
        for column in row:
            str_row[column] = row[column]
        table.append(str_row)

    file_handle.close()
    return table

covid_csv = loop_and_create(file_path)

def main() -> None:
    """Main implementation of the program."""
    print("Please give the type of data wanted. Options: Comparison, (for a given country or continent) singular value at a date, all data at a date, charted data for an operation.")

    print("Choose data")

    print("Choose country either continent")
    
    print("Choose a country or type World")

    print("Choose a continent")

    print("Do you want line or bar graph?")

    print("Do you want Pi chart or bar chart?")

    list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,0 ,10, 11, 20, 22, 30]

    dict: Dict(str, float) = {
        "A": 100,
        "B": 20,
        "C": 1,
        "D": 25,
        "E": 15,
        "G": 10,
        "H": 11,
        "I": 9,
        "J": 15,
        "K": 22    }

    print(continent_country_compare)

    return None

# List of all countries and continents in the data set

def find_total_countries_continents(option: str) -> List[str]:
    """Finds valid countries and puts it in a list."""
    dupe_countries: List[str] = []
    for row in covid_csv:
        dupe_countries.append(row[option])

    return dupe_countries


# List of all continents in the data set
def find_total_continents() -> List[str]:
    """Finds valid continents and puts it in a list."""
    dupe_continent: List[str] = []
    for rows in covid_csv:
        dupe_continent.append(rows["continent"])
    
    return dupe_continent

# BELOW FUNCTION IS USED IN OTHERS, DO NOT PUT IN MAIN

def duplicate_hunter(data_set: List[str]) -> List[str]:
    duplicate_free_list: List[str] = []
    for x in data_set:
        if x not in duplicate_free_list:
            duplicate_free_list.append(x)
    return duplicate_free_list

valid_countries: List[str] = duplicate_hunter(find_total_countries_continents("location"))
valid_continents: List[str] = duplicate_hunter(find_total_countries_continents("continent"))

####### Below, the function is used in another... DO NOT DIRECTLY IMPLEMENT INTO MAIN

def list_of_desired_value_by_continent_by_date(Date: str, Continent: str, Chosen_Column: str) -> List[int]:
    """The list operation should produce and print a List[float].
        
    This is for each of the Chosen_Column argument’s values in a row whose 
    location column contains the targeted continent at the targeted date.
    For a total of the values, see the desired_value_by_continent_at_date_total function!
    """

    READ_MODE = "r"
    file_path = "NCHack_2020/Covid_Data.csv"
    file_handle = open(file_path, READ_MODE, encoding="utf8")
    covid_csv = DictReader(file_handle)

   # file_handle = open(file_path, READ_MODE, encoding="utf8")
   # csv_reader = DictReader(file_handle)
    List_Of_Dictionaries_0: List[Dict[str, str]] = []
    List_Of_Dictionaries_1: List[Dict[str, str]] = []
    List_Of_Dictionaries_2: List[Dict[str, float]] = []

    for row in covid_csv:
            if row["date"] == Date:
                List_Of_Dictionaries_0.append(row)

    for row in List_Of_Dictionaries_0:
        if row["continent"] == Continent:
            List_Of_Dictionaries_1.append(row)
    
    for row in List_Of_Dictionaries_1:
        float_row: Dict[str, float] = {}
        for column in row:
            try:
                float_row[column] = float(row[column])
            except ValueError:
                ...
        List_Of_Dictionaries_2.append(float_row)


    Return_List: List[Dict[str, float]] = []

    for dictionary in List_Of_Dictionaries_2:
        try:
            Return_List.append(dictionary[Chosen_Column])
        except KeyError:
            ...

    return Return_List

### ^^ Used in another function... 

def find_dates(country: str) -> List[str]:
    """Searches through our covid csv and for each country it will give a list of the dates."""
    dates: List[str] = []
    for row in covid_csv:
        if row["location"] == country:
            dates.append(row["date"])
            
    return dates

def desired_value_by_country_at_date(Date: str, Country: str, Chosen_Column: str) -> List[int]:
    """The list operation should produce and print a List[float].
        
    This is for each of the Chosen_Column argument’s values in a row whose 
    location column contains the targeted Country.
    """

   # file_handle = open(file_path, READ_MODE, encoding="utf8")
   # csv_reader = DictReader(file_handle)
    List_Of_Dictionaries_0: List[Dict[str, str]] = []
    List_Of_Dictionaries_1: List[Dict[str, str]] = []
    List_Of_Dictionaries_2: List[Dict[str, float]] = []

    for row in covid_csv:
        if row["date"] == Date:
            List_Of_Dictionaries_0.append(row)

    for row in List_Of_Dictionaries_0:
        if row["location"] == Country:
            List_Of_Dictionaries_1.append(row)
    
    for row in List_Of_Dictionaries_1:
        float_row: Dict[str, float] = {}
        for column in row:
            try:
                float_row[column] = float(row[column])
            except ValueError:
                ...
        List_Of_Dictionaries_2.append(float_row)
    Return_List: List[Dict[str, float]] = []

    for dictionary in List_Of_Dictionaries_2:
        try:
            Return_List.append(dictionary[Chosen_Column])
        except KeyError:
            ...

    return Return_List

# BELOW FUNCTION IMPLEMENT INTO MAIN
def desired_value_by_country_at_date_list(Date: str, Country: str, Chosen_Column: str) -> List[int]:
    """The list operation should produce and print.
        
    This is for each of the Chosen_Column argument’s values in a row whose 
    location column contains the targeted Country.
    """

   # file_handle = open(file_path, READ_MODE, encoding="utf8")
   # csv_reader = DictReader(file_handle)
    List_Of_Dictionaries_0: List[Dict[str, str]] = []
    List_Of_Dictionaries_1: List[Dict[str, str]] = []
    List_Of_Dictionaries_2: List[Dict[str, float]] = []

    for row in covid_csv:
        if row["date"] == Date:
            List_Of_Dictionaries_0.append(row)

    for row in List_Of_Dictionaries_0:
        if row["location"] == Country:
            List_Of_Dictionaries_1.append(row)
    
    for row in List_Of_Dictionaries_1:
        float_row: Dict[str, float] = {}
        for column in row:
            try:
                float_row[column] = float(row[column])
            except ValueError:
                ...
        List_Of_Dictionaries_2.append(float_row)
    Return_List: List[Dict[str, float]] = []

    for dictionary in List_Of_Dictionaries_2:
        try:
            Return_List.append(dictionary[Chosen_Column])
        except KeyError:
            ...

    return Return_List[0]

# Below Function Implement in main
def desired_value_by_continent_at_date_total(Date: str, Country: str, Chosen_Column: str) -> List[int]:
    return sum(list_of_desired_value_by_continent_by_date(Date, Country, Chosen_Column))

    
def top_ten(data: List[float]) -> List[float]:
    """Takes in a list of floats and gives the top ten"""
    new_data: List = []
    data_copy: List = []
    for y in data:
        data_copy.append(y)
    i = 0
    if len(data_copy) < 10:
        return data_copy

    while i < 10:
        for x in range(0, len(data_copy)):
            if data_copy[x] == max(data_copy):
                new_data.append(data_copy[x])
                data_copy.pop(x)
                break
        
        i += 1

    return new_data



def list_of_values_at_date_at_operation(date: str, operation: str, continent_or_location: str) -> List[List[str]]:
    results: List[List[str]] = []
    for row in covid_csv:
        if row["date"] == date and row["location"] != "World" and row["location"] != "International":
            location_to_value: List[str] = []
            location_to_value.append(row[continent_or_location])
            location_to_value.append(row[operation])
            results.append(location_to_value)
            
    return results



def top_ten_dict(data: Dict[str, float]) -> Dict[str, float]:
    """Takes in a list of floats and gives the top ten"""
    new_data: Dict(str, float) = Dict()
    data_copy: Dict(str, float) = Dict()
    for key in data:
        data_copy[key] = data[key]
        
    i = 0
    if len(data_copy) < 10:
        return data_copy

    while i < 10:
        for location in data_copy:
            if location == max(data_copy, key=lambda key: data_copy[key]):
                new_data[location] = data_copy[location]
                data_copy.pop(location)
                break
        i += 1

    return new_data

if __name__ == "__main__":
    main()