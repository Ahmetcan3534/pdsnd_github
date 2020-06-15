import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' } 

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june'] #created list for later reference

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] #created list for later reference

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
    city = input('Please select city: Chicago, New York City or Washington.')
    while city.lower() not in ['chicago', 'new york city', 'washington']: #spelling check
        city = input('Invalid city. Please check spelling. Chicago, New York City or Washington.')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please select month: all, january, february, march, april, may or june.')
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']: #spelling check
        month = input('Invalid month. Please check spelling. all, january, february, march, april, may or june.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select day of the week: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday.')
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']: #spelling check
        day = input('Invalid day. Please check spelling. all, monday, tuesday, wednesday, thursday, friday, saturday, sunday.')

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time']) #start time formatted to datetime
    df['End Time'] = pd.to_datetime(df['End Time']) #end time formatted to datetime
    df['Month'] = df['Start Time'].dt.month #new column for month
    df['Day'] = df['Start Time'].dt.dayofweek #new column for day
    df['Hour'] = df['Start Time'].dt.hour #new column for hour
    df['Start-to-End Station'] = df['Start Station'] + ' to ' + df['End Station'] #new column for start-to-end station 
        
    if month.lower() != 'all': #filter check: checking to see if month is filtered
        df = df[df['Month'] == MONTHS.index(month.lower()) + 1] #filtered month indexed from previously created list
    
    if day.lower() != 'all': #filter check: checking to see if day is filtered
        df = df[df['Day'] == DAYS.index(day.lower())] #filtered day indexed from previously created list
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    most_common_month = MONTHS[df['Month'].mode()[0] -1] #-1 added to the index because dataframe starts months at 1, while our list starts at 0
    print('Most common month is: ' + str(most_common_month))
    
    # TO DO: display the most common day of week
    most_common_day = DAYS[df['Day'].mode()[0]] #mode of weekday
    print('Most common day is: ' + str(most_common_day))
    
    # TO DO: display the most common start hour
    most_common_hour = df['Hour'].mode()[0] #mode of hours
    print('Most common hour of the day is: ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    insight = input('Would you like to see 5 rows of raw data? (Y/N)') #input to demand raw data
    starting_row = 1
    last_row = 5    
    
    while insight.lower() not in ['y', 'n', 'yes', 'no']: #input validation
        insight = input('Invalid input. Please answer yes, no, y or n.')
    
    while insight.lower() in ['y', 'yes']:
        raw_data = df.loc[df.index[starting_row:(last_row +1)],['Month','Day','Hour']] #slicing relevant columns of the function
        print(raw_data)
        insight = input('Would you like to see 5 more rows of raw data? (Y/N)')
        while insight.lower() not in ['y', 'n', 'yes', 'no']: #to make sure invalid inputs can not accidentally run the program further
            insight = input('Invalid input. Please answer yes, no, y or n.')        
        if insight.lower() in ['y', 'yes']: #adding 5 to rows for further inspection
            starting_row += 5
            last_row += 5      
                   
        
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0] #mode of start stations
    print('Most common start station is: ' + str(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0] #mode of end stations
    print('Most common end station is: ' + str(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_to_end_station = df['Start-to-End Station'].mode()[0] #mode of start-to-end stations
    print('Most frequent start-to-end station is: ' + str(most_common_start_to_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    insight = input('Would you like to see 5 rows of raw data? (Y/N)') #input to demand raw data
    starting_row = 1
    last_row = 5    
    
    while insight.lower() not in ['y', 'n', 'yes', 'no']:
        insight = input('Invalid input. Please answer yes, no, y or n.')
    
    while insight.lower() in ['y', 'yes']:
        raw_data = df.loc[df.index[starting_row:(last_row +1)],['Start Station','End Station','Start-to-End Station']]
        print(raw_data)
        insight = input('Would you like to see 5 more rows of raw data? (Y/N)')
        while insight.lower() not in ['y', 'n', 'yes', 'no']:
            insight = input('Invalid input. Please answer yes, no, y or n.')        
        if insight.lower() in ['y', 'yes']:
            starting_row += 5
            last_row += 5    
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Total Travel Time'] = (df['End Time'] - df['Start Time']) #total travel time calculated
    print('Total travel time is: ' + str(df['Total Travel Time'].sum())) #total travel time summed

    # TO DO: display mean travel time
    print('Mean travel time is: ' + str(df['Total Travel Time'].mean())) #mean of total travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    insight = input('Would you like to see 5 rows of raw data? (Y/N)') #input to demand raw data
    starting_row = 1
    last_row = 5    
    
    while insight.lower() not in ['y', 'n', 'yes', 'no']:
        insight = input('Invalid input. Please answer yes, no, y or n.')
    
    while insight.lower() in ['y', 'yes']:
        raw_data = df.loc[df.index[starting_row:(last_row +1)],['Start Time','End Time','Total Travel Time']]
        print(raw_data)
        insight = input('Would you like to see 5 more rows of raw data? (Y/N)')
        while insight.lower() not in ['y', 'n', 'yes', 'no']:
            insight = input('Invalid input. Please answer yes, no, y or n.')        
        if insight.lower() in ['y', 'yes']:
            starting_row += 5
            last_row += 5
    
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
   
    # TO DO: Display counts of user types
    tmp = df.groupby(['User Type']).count() #created temporary dataframe for user type count
    tmp['Count'] = tmp['Start Time'] #selected any column in our temporary dataframe to work as our count column to eliminate repetitive displaying
    print(tmp['Count'])

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: #Gender column doesn't exist in all csv files, so we use an if statement to check for it. I found the columns method on the web
        tmp = df.groupby(['Gender']).count() #created temporary dataframe for Gender count
        tmp['Count'] = tmp['Start Time'] #selected any column in our temporary dataframe to work as our count column to eliminate repetitive displaying
        print(tmp['Count'])

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: #Birth Year column doesn't exist in all csv files, so we use an if statement to check for it
        most_common_birth_year = df['Birth Year'].mode()[0] #mode of birth years
        print('Most common birth year is: ' + str(most_common_birth_year))

        earliest_birth_year = df['Birth Year'].min() #min of birth years
        print('Earliest birth year is: ' + str(earliest_birth_year))

        most_recent_birth_year = df['Birth Year'].max() #max of birth years
        print('Most recent birth year is: ' + str(most_recent_birth_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    insight = input('Would you like to see 5 rows of raw data? (Y/N)') #input to demand raw data
    starting_row = 1
    last_row = 5    
    
    while insight.lower() not in ['y', 'n', 'yes', 'no']:
        insight = input('Invalid input. Please answer yes, no, y or n.')
    
    while insight.lower() in ['y', 'yes']:
        raw_data = df.loc[df.index[starting_row:(last_row +1)],['User Type','Gender','Birth Year']]
        print(raw_data)
        insight = input('Would you like to see 5 more rows of raw data? (Y/N)')
        while insight.lower() not in ['y', 'n', 'yes', 'no']:
            insight = input('Invalid input. Please answer yes, no, y or n.')        
        if insight.lower() in ['y', 'yes']:
            starting_row += 5
            last_row += 5
            
    print('-'*40)


def main():
    while True:
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
