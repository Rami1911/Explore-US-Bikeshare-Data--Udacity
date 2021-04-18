import time
import pandas as pd
import numpy as np
from tabulate import tabulate
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'nyc':'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=str(input("Which city would you like to choose to show its data? Choose from Chicago,New York City, Washington:\n")).lower()
            if city in ['chicago',"new york city","washington","nyc"]:
             break
            else:
                print("This city is not included, try chicago or new york city or washington: \n")

        except ValueError:
            print("Thats not appropriate,try using this structure, ex: cairo \n ")


    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month=str(input("Which month would you like to choose to show its data, if you need all type (all):\n")).lower()
            if month in ["january","february","march","april","may","june","all"]:
             break
            else:
                print("This month is not included, try months form january to june:\n ")

        except ValueError:
            print("Thats not appropriate try using this structure, ex: january\n ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=str(input("Which day would you like to choose to show its data,if you need all type (all):\n")).lower()
            if day in ["saturday","sunday","monday","tuesday","wednesday","thursday","friday","all"]:
             break
            else:
                print("\nThis is not valid, please try again  ")

        except ValueError:
            print("\nThats not appropriate try using this structure, ex: thursday ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename=CITY_DATA[city]
    df=pd.read_csv(filename)

    #convert the Start Time to date times
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    #extract the month and day to create new coulumn
    df["month"]=df["Start Time"].dt.month
    df["day_of_week"]=df["Start Time"].dt.day_name()

    if month !="all":
        months=["january","february","march","april","may","june"]
        month=months.index(month)+1

        df=df[df["month"]==month]

    if day !="all":
        df=df[df["day_of_week"]==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nThe most common month is : ",df["month"].mode()[0])

    # display the most common day of week
    print("\nThe most common day is : ",df["day_of_week"].mode()[0])

    # display the most common start hour
    df["hour"]=df["Start Time"].dt.hour
    print("\nThe most common hour is : ",df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nThe most commonly used start station:",df["Start Station"].mode()[0])

    # display most commonly used end station
    print("\nThe most commonly used end station:",df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    df["combination"]= df["Start Station"] +" and "+ df["End Station"]
    print("\nThe most frequant duration is:",df["combination"].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\nThe total Traveled time is: ",df["Trip Duration"].sum())

    # display mean travel time
    print("\nThe average Traveled time is: ",df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 #Data display Function to ask the user to show the Data
"""
def data_display(df):
      view_data=str(input("\n Would you like to show the 5 rows of individual data, kindly type yes or no :\n")).lower()
      sl=0 #starting location
      while (view_data=="yes"):

          print(df.iloc[0:sl+5])
          sl+=5
          view_data=str(input("\n Would you like to continue, kindly type yes or no :\n")).lower()
"""

def user_stats(df):#add city to the arguments for th if condition
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #subscriber=0
    #customer=0
    #dep=0

    # Display counts of user types

    """
    for user in df["User Type"]:
        if user == "Subscriber":
         subscriber+=1
    #print("The count of Users: ",df["User Type"].count())
        elif user == "Customer" :
         customer+=1
        else:
         dep+=1
    print("The User Type Count is :\nSubscriber: {} \nCustomer: {}\nDependant: {}".format(subscriber,customer,dep))
    print("\nThe total Count of Users: {} ".format(subscriber+customer+dep))
"""
    print("\nThe total Count of Users:\n",df["User Type"].value_counts())
    # Display counts of gender if city != washington
    if city != "washington":
        print("\nThe count of gender: ",df.groupby(["Gender"])["Gender"].count())
        print("\nThe total count of gender: ",df["Gender"].count())
        # Display earliest, most recent, and most common year of birth


        print(" \nThe earliest year of birth is:",df["Birth Year"].min())
        print(" \nThe most recent year of birth is:",df["Birth Year"].max())
        print(" \nThe most common year of birth is:",df["Birth Year"].mode()[0])
    i=0
    while True:

       display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
       pd.set_option('display.max_columns',200)
       if display_data.lower() != 'yes':
        break
       print(tabulate(df.iloc[np.arange(0+i,5+i)], headers ="keys", tablefmt="pretty"))
       print("\n\n")
       i+=5


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        global city
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
