"""Data analysis file for Covid_Data_Bot"""

from typing import Dict, List 
from csv import DictReader

READ_MODE = "r"
file_path = "Covid_Data.csv"
file_handle = open(file_path, READ_MODE, encoding="utf8")
covid_csv = DictReader(file_handle)



def main() -> None:
    """Main implementation of the program."""
    valid_countries: List[str] = duplicate_hunter(find_total_countries())
    valid_continents: List[str] = duplicate_hunter(find_total_continents())
    print(valid_continents)

    return None

# List of all countries in the data set

def find_total_countries() -> List[str]:
    """Finds valid countries and puts it in a list."""
    dupe_countries: List[str] = []
    for row in covid_csv:
        dupe_countries.append(row["location"])
    
    
    return dupe_countries


# List of all continents in the data set
def find_total_continents() -> List[str]:
    """Finds valid continents and puts it in a list."""
    dupe_continent: List[str] = []
    for row in covid_csv:
        dupe_continent.append(row["continent"])
    
    return dupe_continent


def duplicate_hunter(data_set: List[str]) -> List[str]:
    duplicate_free_list: List[str] = []
    for x in data_set:
        if x not in duplicate_free_list:
            duplicate_free_list.append(x)
    return duplicate_free_list


##### NEEDS A LIST OF DICTIONARIES CONTAINING THE COUNTRY
def list_of_desired_value(Country: str, Chosen_Column: str) -> List[int]:
    """The list operation should produce and print a List[float].
        
    This is for each of the Chosen_Column argument’s values in a row whose 
    location column contains the targeted Country.
    """

   # file_handle = open(file_path, READ_MODE, encoding="utf8")
   # csv_reader = DictReader(file_handle)
    List_Of_Dictionaries_1: List[Dict[str, str]] = []
    List_Of_Dictionaries_2: List[Dict[str, float]] = []

    for row in covid_csv:
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
#############


#############
    Return_List: List[Dict[str, float]] = []

    for dictionary in List_Of_Dictionaries_2:
        try:
            Return_List.append(dictionary[Chosen_Column])
        except KeyError:
            ...

    return Return_List

        

def find_dates(country: str) -> List[str]:
    """Searches through our covid csv and for each country it will give a list of the dates."""
    dates: List[str] = []
    for row in covid_csv:
        if row["location"] == country:
            dates.append[row["date"]]
            
    return dates


if __name__ == "__main__":
    main()


