import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ['chicago','washington','new york city']
    while True:
        try:
            city = (input('Enter a city: washington, chicago or new york city \n').lower())
            if city in cities:
                print("Pulling data from desired city...")
                break
            else:
                print('Oops! you entered an invalid city. Please try again')
                print()
        except:
            print('That is not a valid city!')
           
            df['cit']= df.assign(city)
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ['january','february','march','april','may','june','all']
    while True:
        try:
            month = (input('Enter a desired month from january to june or select "all": \n').lower())
            if month in months:
                print("Filtering by required month...")
                break
            else:
                print('Oops! you entered an invalid month. Please try again')
                print()
        except:
            print('That is not a valid month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        try:
            day = (input('Enter a desired day of week: \n').lower())
            if day in days:
                print('Filtering by desired day of week...')
                break
            else:
                print('That\'s not a valid day of week! please try again')
                print()
        except:
            print('That is not a valid day of week! Please try again')

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
        
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
                   
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
                     
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month: {}',common_month)
    print()

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day_of_week: {}',popular_day)
    print()

    # TO DO: display the most common start hour
    
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: ',popular_hour)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is ',common_start)
    print()

    # TO DO: display most commonly used end station
    commonly_usedend = df['End Station'].mode()[0]
    print('The most commonly used end station is ',commonly_usedend)
    print()

    # TO DO: display most frequent combination of start station and end station trip
    df['common'] = df[['Start Station', 'End Station']].apply(lambda x: ' and '.join(x), axis=1)
    common_combination = df['common'].mode()[0]
    print('The most frequent combination of start station and end station is ',common_combination)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    travel = travel_time/60
    print('The total travel time is {} hours '.format(travel))
    print()

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    mean_travel = travel_mean/60
    print('The mean travel time is {} hours'.format(mean_travel))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There are {} different types of users'.format(user_types))
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('The total gender is ',gender)
        print()
    else:
        print('Oops! Sorry, there\'s no value for gender in Washington')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_birth = df['Birth Year'].max()
        print('The most recent year of birth is ',early_birth)
        print()
        
        recent_birth = df['Birth Year'].min()
        print('The earliest year of birth is ',recent_birth)
        print()
        
        common_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth is ',common_birth)
        print()
    else:
        print('Oops! Sorry, there\'s no value for Birth Year in Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    row_length = df.shape[0]
    for i in range(0, row_length, 5):
        yes = input("\nWould you like to examine five lines of the raw data? Type 'yes' or 'no': \n")
        if yes.lower() != 'yes':
            break
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no: \n')
        if restart.lower() != 'yes':
            print("Thanks for your time!")
            break


if __name__ == "__main__":
	main()
