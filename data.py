"""Data analysis file for Covid_Data_Bot"""

# from test import list_of_values_at_date_at_operation
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
    print(
    "Welcome to the COVID Data Bot!!! This program uses a publicly\n",
    "available data set, published daily, to find requested COVID\n", 
    "Statistics on any country or continent in the world (including",
    "the world statistics)!\n"
    )
    print("Do you want a comparison of data between countries, continents,\n",
          "or the world, or do you want a singular value for any of these?\n",
          "Type 'Comparison' or 'Single Value')")
    comparison_Response: str = input("Type: ")
    # Run a checker to see if the response to comparision is valid
    valid_countries: List[str] = \
        duplicate_hunter(find_total_countries_continents("location"))
    valid_continents: List[str] = \
        duplicate_hunter(find_total_countries_continents("continent"))
    
    if comparison_Response.lower() == "comparison":
        # Run whole different process for a comparison
        # which country would you like to compare?
        # make pie chart or multiple line chart
        ...
    if comparison_Response.lower() == "single value":
        print("Please put in the country or continent of interest (capitalized)! Or type World!")

        region: str = input("Region: ")
        is_country: bool = False
        is_continent: bool = False
        
        if region in valid_countries:
            is_country = True        
        if region in valid_continents:
            is_continent = True
        if not (is_country or is_continent):
            sys.exit("You gave an invalid country or continent. Run the"+
                     "program again.")
        print("Please put in the statistic you want to know! We support",
              "the following statistics in the same format:",
              "\ntotal_cases"
              "\nnew_cases",
              "\ntotal_deaths",
              "\nnew_deaths",
              "\ntotal_cases_per_million",
              "\nnew_cases_per_million",
              "\ntotal_deaths_per_million",
              "\nnew_deaths_per_million",
              "\nnew_tests, total_tests",
              "\ntotal_tests_per_thousand",
              "\nnew_tests_per_thousand",
              "\ntests_per_case",
              "\npositive_rate",
              "\ntests_units")
        
        statistic: str = input("Statistic: ")
        if not valid_operation_checker(statistic):
            sys.exit("The given statistic was either not supplied in the\n" +
                     "correct format or was not in the list. Run the program" +
                     "again.")
        print("Do you want a statistic list for all of COVID or the value at\n",
              "a certain date? Type 'all' for the whole list, or a date for\n",
              "the data at the date in the format: MM/DD/YYYY.")

        date: str = input("date: ")        
        if not date_checker(date):
            sys.exit("The given date is either pre-2020, post-2020," +
                     "or has not happened yet! Run the program again.")
        if date != "all":
            if is_country:
                # We will then run the operation to get the requested statistic in the country at the date
                print(desired_value_by_country_at_date(date, region, statistic))
            if is_continent:
                # We will then run the operation to get the requested statistic in the continent at the date 
                print(desired_value_by_continent_at_date_total(date, region, statistic))
        else:
            if is_country:
                # We will then run the operation to get the requested statistic list over the course of 2020.
                output_array: List[int] = desired_value_by_country_list(
                                          region, 
                                          statistic)
                print(desired_value_by_country_list(region, statistic))
                print("Would you like a graph form? 'Yes' or 'No'")
                response_to_graph: str = input("Graph? ")
                if response_to_graph.lower() == "yes":
                    make_line_chart(output_array, find_dates(
                                    region),
                                    statistic)
                elif response_to_graph.lower() == "no":
                    print("Okay, no charting of the data!")
                else:
                    sys.exit("You did not give a yes or a no. Run the program again.")
            if is_continent is True:
                print("Would you like a graph for? 'Yes' or 'No'")
                
                response_to_graph: str = input("Graph? ")
                if response_to_graph.lower() == "yes":
                    # We will then make a chart of the data
                    ...
                if response_to_graph.lower() == "no":
                    print("Okay, no charting of the data!")
        print("Data requested was supplied!")            

    
def valid_operation_checker(operation: str) -> bool:
    """Checks for valid operation given an operation as argument."""
    valid_operation_list: List[str] = ["total_cases", "new_cases",
                                       "total_deaths",
                                       "new_deaths", "total_cases_per_million",
                                       "new_cases_per_million",
                                       "total_deaths_per_million",
                                       "new_deaths_per_million", "new_tests",
                                       "total_tests",
                                       "total_tests_per_thousand",
                                       "new_tests_per_thousand",
                                       "tests_per_case", "positive_rate",
                                       "tests_units"]
    if operation in valid_operation_list:
        return True
    else: 
        return False


def countries_in_continents(continent: str) -> List[str]:
    """Return a list of countries per continent input."""
    countries: List[str] = []
    
    for row in covid_csv:
        if row["continent"] == continent and row["location"] not in countries:
            countries.append(row["location"])

    return countries


def find_total_countries_continents(option: str) -> List[str]:
    """Finds valid countries and puts it in a list."""
    dupe_countries: List[str] = []
    for row in covid_csv:
        try:
            dupe_countries.append(row[option])
        except:
            ValueError()

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


def date_checker(date: str) -> bool:
    dates: List[str] = []
    for row in covid_csv:
        dates.append(row["date"])
    if date in dates or date == "all":
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

def desired_value_by_country_list(country: str, 
                                  chosen_column: str) -> List[int]:
    """The list operation should produce and print a List[int].
        
    This is for each of the chosen_column argument’s values in a row whose 
    location column contains the targeted country.
    """
    return_list: List[int] = []

    for row in covid_csv:
        if row["location"] == country:
            try:
                return_list.append(int(row[chosen_column]))
            except ValueError:
                return_list.append(0)

    return return_list
    
# BELOW FUNCTION IMPLEMENT INTO MAIN
def desired_value_by_country_at_date(date: str, country: str, chosen_column: str) -> int:
    """The operation takes a date, country, and chosen column and returns a float.
        
    This is for each of the chosen_column argument’s values in a row whose 
    location column contains the targeted country at the given date
    """
    for row in covid_csv:
        if row["location"] == country and row["date"] == date:
                return int(row[chosen_column])
        
    return 0


# Below Function Implement in main
def desired_value_by_continent_at_date_total(date: str, continent: str, chosen_column: str) -> int:
    return_int: int = 0

    for row in covid_csv:
        if row["date"] == date and row["continent"] == continent:
            return_int += int(row[chosen_column])

    return return_int


def list_of_values_at_date_at_operation(date: str, operation: str, continent_or_location: str) -> List[List[str]]:
    results: List[List[str]] = []
    for row in covid_csv:
        if row["date"] == date and row["location"] != "World" and row["location"] != "International":
            location_to_value: List[str] = []
            location_to_value.append(row[continent_or_location])
            location_to_value.append(row[operation])
            results.append(location_to_value)
            
    return results


def top_ten(data: List[int]) -> List[int]:
    """Takes in a list of floats and gives the top ten"""
    new_data: List[int] = []
    data_copy: List[int] = []
    for y in data:
        data_copy.append(y)
    
    if len(data_copy) < 10:
        return data_copy

    i: int = 0
    while i < 10:
        for x in range(0, len(data_copy)):
            if data_copy[x] == max(data_copy):
                new_data.append(data_copy[x])
                data_copy.pop(x)
                break
        i += 1
    return data_copy


def top_15_dict(data: Dict[str, float]) -> Dict[str, float]:
    """Takes in a list of floats and gives the top 15"""
    new_data: Dict[str, float] = {}
    data_copy: Dict[str, float] = {}
    for key in data:
        data_copy[key] = data[key]
        
    i = 0
    if len(data_copy) < 15:
        return data_copy

    while i < 15:
        for location in data_copy:
            if location == max(data_copy, key=lambda key: data_copy[key]):
                new_data[location] = data_copy[location]
                data_copy.pop(location)
                break
        i += 1

    return new_data


def top_seven_dict(data: Dict[str, float]) -> Dict[str, float]:
    """Takes in a list of floats and gives the top ten"""
    new_data: Dict[str, float] = {}
    data_copy: Dict[str, float] = {}
    for key in data:
        data_copy[key] = data[key]
        
    i = 0
    if len(data_copy) < 7:
        return data_copy

    while i < 7:
        for location in data_copy:
            if location == max(data_copy, key=lambda key: data_copy[key]):
                new_data[location] = data_copy[location]
                data_copy.pop(location)
                break
        i += 1

    return new_data


def make_bar_chart_compare(operation: str, location_or_continent: str, date: str) -> None:
    """Bar charts the data of top 10 countries of continents at a date."""
    pyplot.title(operation + " at " + date)
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

    condensed_values: Dict[str, float] = top_15_dict(dict_index)

    y_values: List[float] = []
    for key in condensed_values:
        y_values.append(condensed_values[key])   
    
    x_locations: List[str] = []
    for key in condensed_values:
        x_locations.append(key)

    pyplot.bar(x_locations, y_values)
    pyplot.show()


def make_pie_chart_compare(operation: str, location_or_continent: str, date: str) -> None:
    """Pie charts the data of top 10 countries of continents at a date."""

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


    condensed_values: Dict[str, float] = top_seven_dict(dict_index)

    y_values: List[float] = []
    for key in condensed_values:
        y_values.append(condensed_values[key])   
    
    x_locations: List[str] = []
    for key in condensed_values:
        x_locations.append(key)



    
    labels = x_locations
    sizes = y_values
    colors = ["red", "blue", "green", "yellow", "purple", "brown", "teal", "pink", "lightcoral", "lightskyblue"]
    explode = (0.1, 0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow= False, startangle=90, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f"{operation} at {date}")
    plt.show()
    return None
        
    
def make_line_chart(data: List[int], date: List[str], operation: str) -> None:
    """Makes a chart."""
    plt.plot(date, data)
    plt.xlabel("date")
    plt.ylabel(operation)
    plt.show()
    return None

if __name__ == "__main__":
    main()