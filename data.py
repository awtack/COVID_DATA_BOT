"""Data analysis file for Covid_Data_Bot"""

from typing import Dict, List 
from csv import DictReader

READ_MODE = "r"
file_path = "Covid_Data.csv"
file_handle = open(file_path, READ_MODE, encoding="utf8")
covid_csv_file = DictReader(file_handle)



def main() -> None:
    """Main implementation of the program."""
    

    print(valid_continents)

    return None

# List of all countries and continents in the data set

def find_total_countries_continents(option: str) -> List[str]:
    """Finds valid countries and puts it in a list."""
    dupe_countries: List[str] = []
    for row in covid_csv_file:
        dupe_countries.append(row[option])
    
    
    return dupe_countries


# List of all continents in the data set
def find_total_continents() -> List[str]:
    """Finds valid continents and puts it in a list."""
    dupe_continent: List[str] = []
    for rows in covid_csv_file:
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
            dates.append[row["date"]]
            
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



if __name__ == "__main__":
    main()


file_handle.close()