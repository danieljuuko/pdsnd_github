import time
import pandas as pd
import numpy as np
from IPython.display import display
while True:
    starts = input('\nHello! Would you like to get some US bikeshare data? Enter yes or no.\n')
    CITY_DATA = { 'Chicago': 'chicago.csv',
                  'New york city': 'new_york_city.csv',
                  'Washington': 'washington.csv' }

    def get_filters():
        """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
        print('Okay then, Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

        citys=['Chicago', 'New york city', 'Washington']
        city=""
        while city not in citys:
            city=str(input("Enter the city (Chicago, New york city, Washington): "))
            city=city.title()
            if city == 'New York City':
                city='New york city'

        year=['All','January','February ','March','April','May','June','July','August','September','October','November','December']
        month=""
        while month not in year:
            month = str(input("Enter the month(all,January,February, ... December): "))
            month=month.title()

        week=['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day=""
        while day not in week:
            day=str(input("Enter the day(all, Monday, Tuesday, ... Sunday): "))
            day=day.title()

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
        df.rename( columns={'Unnamed: 0':'Trip_id'}, inplace=True )

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month_input'] = df['Start Time'].dt.month

        look_up = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
                6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


        df['month_input'] = df['month_input'].apply(lambda x: look_up[x])
        df['day_input'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        if (month =='All' and day =='All'):
            df = df
        if (month != 'All'):
            df= df[df['month_input'].isin([month])]
        if (day != 'All'):
            df= df[df['day_input'].isin([day])]
        if (month !='All' and day !='All'):
            df = df[df['month_input'].isin([month])& df['day_input'].isin([day])]

        #print(df)

        return df


    def time_stats(df):
        """Displays statistics on the most frequent times of travel."""
        startstime = input('\nHello! Would you like to get some US bikeshare about the Most Frequent Times of Travel? Enter yes or no.\n')
        while startstime.lower() == 'yes':



            start_time = time.time()

            # TO DO: display the most common month, TO DO: display the most common day of week, TO DO: display the most common start hour

            display('Most common month is',df.month_input.mode().to_string(index=False),', Most common day of week is',df.day_input.mode().to_string(index=False),', Most common start hour is ',df.hour.mode().to_string(index=False))

        #print("This took %s seconds." % (time.time() - start_time))
            print('-'*40)

            break



    def station_stats(df):
        """Displays statistics on the most popular stations and trip."""
        startstation = input('\nHello! Would you like to get some US bikeshare about the Most Popular Stations and Trips? Enter yes or no.\n')
        while startstation.lower() == 'yes':


            start_time = time.time()

            # TO DO: display most commonly used start station, TO DO: display most commonly used end station, TO DO: display most frequent combination of start station and end station trip
            display('Most commonly used start station is',df['Start Station'].mode().to_string(index=False),', Most commonly used end station is',df['End Station'].mode().to_string(index=False),', Most frequent start-end station trip is',df[['Start Station', 'End Station']].apply(lambda x: ''.join(x), axis=1).mode().to_string(index=False))


           # print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break


    def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""
        starttrip = input('\nHello! Would you like to get some US bikeshare about the Trip Durations? Enter yes or no.\n')
        while starttrip.lower() == 'yes':


            start_time = time.time()

            # TO DO: display total travel time, TO DO: display mean travel time
            display('Total travel time is',df['Trip Duration'].sum(),', Mean travel time is',df['Trip Duration'].mean())


            #print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break


    def user_stats(df):
        """Displays statistics on bikeshare users."""
        startuser = input('\nHello! Would you like to get some US bikeshare about the User Stats? Enter yes or no.\n')
        while startuser.lower() == 'yes':


            
            start_time = time.time()

            # TO DO: Display counts of user types

            display('\nCustomers were',df.loc[df['User Type'] == 'Customer','User Type'].count(),', Dependents were',df.loc[df['User Type']  == 'Dependent','User Type'].count(),', Subscribers were',df.loc[df['User Type']  == 'Subscriber','User Type'].count())

            try:
             # TO DO: Display counts of gender
                display('Males were',df.loc[df.Gender == 'Male','Gender'].count(),', Female were',df.loc[df.Gender== 'Female','Gender'].count())

            # TO DO: Display earliest, most recent, and most common year of birth
                df1=df[df['Birth Year']== min(df['Birth Year'])].head(1)
                df2=df[df['Birth Year']== max(df['Birth Year'])].head(1)

                display('Earliest year of birth is',df1['Birth Year'].to_string(index=False),', Most recent year of birth is',df2['Birth Year'].to_string(index=False),', Most common year of birth',df['Birth Year'].mode().to_string(index=False))

            except:
                display('Counts of gender = None \nEarliest year of birth = None\nMost recent year of birth = None\nMost common year of birth = None\n')
            #print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
    if starts.lower() == 'yes':
        break

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
