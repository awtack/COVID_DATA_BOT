"""Data analysis file for Covid_Data_Bot"""

from test import list_of_values_at_date_at_operation
from typing import Dict, List 
from csv import DictReader
from matplotlib import pyplot 
import matplotlib.pyplot as plt
import sys

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
    print("Welcome to the COVID Data Bot!!! This program uses a publicly available data set, published daily, to find requested COVID Statistics on any country or continent in the world (including the world statistics)!")
    print("Do you want a comparison of data between countries, continents, or the world, or do you want a singular value for any of these? Type 'Comparison' or 'Singular Value'")
    comparison_Response: str = input()
    # Run a checker to see if the response to comparision is valid
    valid_countries: List[str] = duplicate_hunter(find_total_countries_continents("location"))
    valid_continents: List[str] = duplicate_hunter(find_total_countries_continents("continent"))
    if comparison_Response == "Comparison":
        # Run whole different process for a comparison
        ...

    if comparison_Response == "Singular Value":

        print("Please put in the country or continent of interest (capitalized)! Or type World!")
        country_or_continent_of_interest: str = input()
        is_country: bool = False
        is_continent: bool = False
        if country_or_continent_of_interest in valid_countries:
            is_country = True
        if country_or_continent_of_interest in valid_continents:
            is_continent = True
        if (is_country and is_continent) == False:
            sys.exit("You gave an invalid country or continent. Run the program again.")
        print("Please put in the statistic you want to know! We support the following statistics in the same format: total_cases, new_cases, total_deaths, new_deaths, total_cases_per_million, new_cases_per_million, total_deaths_per_million, new_deaths_per_million, new_tests, total_tests, total_tests_per_thousand, new_tests_per_thousand, tests_per_case, positive_rate, tests_units")
        statistic: str = input()
        if valid_operation_checker(statistic) == False:
            sys.exit("The given statistic was either not supplied in the correct format or was not in the list. Run the program again.")
        print("Do you want a statistic list for all of COVID or the value at a certain date? Type 'all' for the whole list, or a date for the data at the date in the format: 00/00/0000.")
        date: str = input()
        if date_checker(date) == False:
            sys.exit("The given date is either pre-2020, post-2020, or has not happened yet! Run the program again.")
        if date != "all":
            if is_country == True:
                # We will then run the operation to get the requested statistic in the country at the date
                print(desired_value_by_country_at_date_float(date, country_or_continent_of_interest, statistic))
                
            if is_continent == True:
                # We will then run the operation to get the requested statistic in the continent at the date 
                print(desired_value_by_continent_at_date_total(date, country_or_continent_of_interest, statistic))
    
        else:
            if is_country == True:
                # We will then run the operation to get the requested statistic list over the course of 2020.
                print(desired_value_by_country_list(country_or_continent_of_interest, statistic))
                print("Would you like a graph form? 'Yes' or 'No'")
                response_to_graph: str = input()
                if response_to_graph != ("Yes" or "No"):
                    sys.exit("You did not give a yes or a no. Run the program again.")
                if response_to_graph == "Yes":
                    # We will then make a chart of the data 
                    make_line_
                if response_to_graph == "No":
                    print("Okay, no charting of the data!")
    
            if is_continent is True:
                print("Would you like a graph for? 'Yes' or 'No'")
                response_to_graph: str = input()
                if response_to_graph == "Yes":
                    # We will then make a chart of the data
                    ...
                if response_to_graph == "No":
                    print("Okay, no charting of the data!")
        print("Data requested was supplied!")            

    
def valid_operation_checker(operation: str) -> bool:
    """Checks for valid operation given an operation as argument."""
    valid_operation_list: List[str] = ["total_cases", "new_cases", "total_deaths", "new_deaths", "total_cases_per_million", "new_cases_per_million", "total_deaths_per_million", "new_deaths_per_million", "new_tests", "total_tests", "total_tests_per_thousand", "new_tests_per_thousand", "tests_per_case", "positive_rate", "tests_units"]
    if operation in valid_operation_list:
        return True
    else: 
        return False


# List of all countries and continents in the data set

def find_total_countries_continents(option: str) -> List[str]:
    """Finds valid countries and puts it in a list."""
    dupe_countries: List[str] = []
    for row in covid_csv:
        try:
            dupe_countries.append(row[option])
        except:
            ValueError

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

def date_checker(Date: str) -> bool:
    dates: List[str] = []
    for row in covid_csv:
        dates.append(row["date"])
    
    if Date in dates:
        return True

    return False

def find_dates(country: str) -> List[str]:
    """Searches through our covid csv and for each country it will give a list of the dates."""
    dates: List[str] = []
    for row in covid_csv:
        if row["location"] == country:
            dates.append(row["date"])
            
    return dates

##### Below function Use in Main

def desired_value_by_country_list(Country: str, Chosen_Column: str) -> List[int]:
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
                float_row[column] = 0.0
        List_Of_Dictionaries_2.append(float_row)
    Return_List: List[Dict[str, float]] = []

    for dictionary in List_Of_Dictionaries_2:
        try:
            Return_List.append(dictionary[Chosen_Column])
        except KeyError:
            ...

    return Return_List
    
# BELOW FUNCTION IMPLEMENT INTO MAIN
def desired_value_by_country_at_date_float(Date: str, Country: str, Chosen_Column: str) -> float:
    """The operation takes a date, country, and chosen column and returns a float.
        
    This is for each of the Chosen_Column argument’s values in a row whose 
    location column contains the targeted Country at the given date
    """

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


def list_of_values_at_date_at_operation(date: str, operation: str, continent_or_location: str) -> List[List[str]]:
    results: List[List[str]] = []
    for row in covid_csv:
        if row["date"] == date and row["location"] != "World" and row["location"] != "International":
            location_to_value: List[str] = []
            location_to_value.append(row[continent_or_location])
            location_to_value.append(row[operation])
            results.append(location_to_value)
            
    return results


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


def top_ten_dict(data: Dict[str, float]) -> Dict[str, float]:
    """Takes in a list of floats and gives the top ten"""
    new_data: Dict(str, float) = {}
    data_copy: Dict(str, float) = {}
    for key in data:
        data_copy[key] = data[key]
        
    i = 0
    if len(data_copy) < 10:
        return data_copy

    while i < 10:
        for key in data_copy:
            if data_copy[key] == max(data_copy):
                new_data.append(data_copy[key])
                data_copy.pop(key)
                break
        i += 1


def make_bar_chart_compare(operation: str, location_or_continent: str, date: str) -> None:
    """Bar charts the data of top 10 countries of continents at a date."""
    pyplot.title(operation + "at" + date)
    pyplot.xlabel(operation)
    pyplot.ylabel("Top locations")

    values: List[float] = []
    
    index: List[List[str]] = list_of_values_at_date_at_operation(date, operation, location_or_continent)

    dict_index: Dict[str, float] = {}
    for x in index:
        if x[1] == '':
            values.append(0)
        else:
            values.append(float(x[1]))

    for x in range(0, len(values)): 
        dict_index[index[x][0]] = values[x]

    for x in dict_index:


    condensed_values: List[float] = top_ten(values)      
    
    pyplot.bar(, counts)
    pyplot.show()


def make_pie_chart_compare(operation: str, location_or_continent: str, date: str) -> None:
    """Pie charts the data of top 10 countries of continents at a date."""
    plt.title(f"{operation} at {date}")
    labels = location_or_continent
    sizes = 
    colors = ["red", "blue", "green", "yellow", "purple", "brown", "teal", "pink", "lightcoral", "lightskyblue"]
    plt.pie()
    plt.show()
    return None
        
    
def make_line_chart(data: List[float], date: List[str], operation: str) -> None:
    """Makes a chart."""
    plt.plot(date, data)
    plt.xlabel("Date")
    plt.ylabel(operation)
    plt.show()
    return None

if __name__ == "__main__":
    main()

