import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def filter_data():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("What is the name of the city you want to explore?").lower())
        if city not in ('chicago', 'new york city', 'washington'):
            print("Invalid entry! Choose one of the following: chicago, new york city and washington.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Which month's data do you want to explore?").lower())
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Sorry, I didn't understand that. Choose one of the following: all, january, february, march, april, may, june")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Which day of the week's data do you want to explore?").lower())
        if day not in ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Sorry, I didn't understand that. Choose one of the following: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday")
        else:
            break

    print('-'*40)
    return city, month, day


def data_loading(city, month, day):
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month of travel is = ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of travel is = ', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common month start hour of travel is = ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('The most commonly used start station is = ', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('The most commonly used end station is = ', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    popular_stationcombo = (df['Start Station'] + '/ ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station is = ', popular_stationcombo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tripTime = (df['Trip Duration']).sum()
    print('The total travel time for all trips = ', total_tripTime)

    # TO DO: display mean travel time
    mean_tripTime = (df['Trip Duration']).mean()
    print('The mean travel time for all trips = ', mean_tripTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The breakdown count of user types:\n', user_types)

    try:
        # TO DO: Display counts of gender
        gender_count = (df['Gender']).value_counts()
        print('The breakdown count of gender:\n', gender_count)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birthyear = (df['Birth Year']).min()
        recent_birthyear = (df['Birth Year']).max()
        popular_birthyear = (df['Birth Year']).mode()[0]

        print('The earliest year of birth is = ', earliest_birthyear)
        print('The most recent year of birth is = ', recent_birthyear)
        print('The most common year of birth is = ', popular_birthyear)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to view the next set of row data?: ").lower()

def main():
    while True:
        city, month, day = filter_data()
        df = data_loading(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
