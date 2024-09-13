import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york city', 'washington']  # Define valid cities
    city = input("Which city would you like to review: Chicago, New York City, or Washington? ").strip().lower()

    while city not in valid_cities:
        print("That is not an option. Please try again.") #handle errors in input ##git is much more intuitive to me
        city = input("Which city would you like to review: Chicago, New York City, or Washington? ").strip().lower() #make case insensitive      

<<<<<<< HEAD
    # TO DO: get user input for month (all, january, february, ... , june) I really hate python. It is not intuitive AT ALL.

    valid_months = ["all", "january", "february", "march", "april", "may", "june"] #define valid months #git is much more intuitive
||||||| parent of 1a0aec5 (fixing the merge error)
    # TO DO: get user input for month (all, january, february, ... , june) ##all this practice really helps
    valid_months = ["all", "january", "february", "march", "april", "may", "june"] #define valid months
=======
    # TO DO: get user input for month (all, january, february, ... , june) 
    valid_months = ["all", "january", "february", "march", "april", "may", "june"] #define valid months
>>>>>>> 1a0aec5 (fixing the merge error)
    month = input("Which month would you like to review: all, january, february, march, april, may, or june? ").strip().lower() #make case insensitive

    while month not in valid_months:
        print("That is not an option. Try again.") #handle errors in input ##can't wait to make a real git repo of my own!!
        month = input("Which month would you like to review: all, january, february, march, april, may, or june? ").strip().lower() #make case insensitive

    print(f"You selected: {city.title()} for the month: {month}.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) I mean it. How are you supposed to know when to use dot notation and when to use ()?
    valid_days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] #define valid days
    day = input("Which day of the week would you like to review? " ).strip().lower() #make case insensitive
        
    while day not in valid_days:
        print("You may only chose all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday.") #handle errors in input
        day = input("Which day of the week would you like to review? ").strip().lower() #make case insensitive

    print(f"You selected day of the week: {day}.")

    print('-'*40)
    return city, month, day
city, month, day = get_filters()

def load_data(city, month, day):
    # print("Entering load_data function")
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # df['City'] = CITY_DATA[city] #checking that city filter actually worked
    print(f"df filtered for {city}.")
    # print(df.head())
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #column_headers = list(df.columns.values)
    #print("Column Headers: ", column_headers)
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    #print(f"df filtered for {month}.")
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #print(f"df filtered for {day}.")
    return df

df = load_data(city, month, day)
# print(df.head())

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    # print("Entering time_stats function")
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].value_counts().idxmax()
    print("The most commonly used start station is ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo = (df.groupby(['Start Station', 'End Station']).size().idxmax())
    print("The most frequent combination of start station and end station is ", popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_time = df["Trip Duration"].sum()
    print("Total travel time is ", tot_time)

    # TO DO: display mean travel time
    av_time = df["Trip Duration"].mean()
    print("Mean travel time is ", av_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(df)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().dropna(axis=0)
    print("The counts of user types are: \n", user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gend = df['Gender'].value_counts().dropna(axis=0)
        print("The counts of gender are \n", gend)
    else:
        print("No gender data available for Washington.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earl = df['Birth Year'].min()
        print("The oldest rider was born in ", earl)
        recent = df["Birth Year"].max()
        print("The youngest rider was born in ", recent)
        comm = df['Birth Year'].mode()[0]
        print("The mosrt common birth year is ", comm)
    else:
        print("No birth year data available for Washington.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
user_stats(df, city)

def display_raw_data(df):
    i = 0
    length = len(df.index)
    raw = input("Would you like to see five rows of the underlying raw data? ").strip().lower() # TO DO: convert the user input to lower case using lower() function
        
    while i < length:
        if raw == 'no':
            break
        elif raw == 'yes': 
            print(df.iloc[i:i+5]) # slicing the DataFrame to display the next five rows
            if i < length:  # Check if there are more rows to display
                raw = input("Would you like to see 5 more rows? ").strip().lower() # converting the user input to lower case using lower() function
                i += 5
            else:
                print("No more rows to display.")
                break
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").strip().lower()
display_raw_data(df)

def main():
    while True:
        #print("entering main function")
        city, month, day = get_filters()
        #print(f"Filters selected - City: {city}, Month: {month}, Day: {day}")
        df = load_data(city, month, day)
        #print("Data loaded successfully")
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
