import datetime as dt
import pandas as pd

def add_minutes_to_datetime(date_string, minutes_to_add):
    # Parse the date string into a datetime object
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    original_datetime = dt.datetime.strptime(date_string, date_format)

    # Add the specified number of minutes
    updated_datetime = original_datetime + dt.timedelta(minutes=minutes_to_add)

    # Convert the updated datetime object back to a string (if needed)
    updated_date_string = updated_datetime.strftime(date_format)

    return updated_date_string


def create_estimated_time(df):
    df['estimated_time'] = df['depart_time']
    # Loop through the rows of the DataFrame
    for i in range(len(df)):
        # Check if the 'status' column is not "on time"
        if df.iloc[i]['status'] != "On Time":
            # Get the current 'estimated_time' value from the DataFrame
            current_time = df.iloc[i]['estimated_time']

            # Extract the first two characters of the 'status' column and convert to an integer
            minutes_late = int(df.iloc[i]['status'][:2])

            # Call the 'add_minutes_to_datetime' function to add 'minutes_late' to 'current_time'
            df.loc[i, 'estimated_time'] = add_minutes_to_datetime(current_time, minutes_late)[:-3] 

     
    return df
  
def seperate_times(df):
    
    df['sched_time'] = pd.to_datetime(df['sched_time'])
    df['day']=df['sched_time'].dt.strftime('%A')
    df['date'] = df['sched_time'].dt.strftime('%Y-%m-%d')  
    df['sched_time'] = df['sched_time'].dt.strftime('%I:%M %p')
    
    df['estimated_time'] = pd.to_datetime(df['estimated_time'])
    df['estimated_time'] = df['estimated_time'].dt.strftime('%I:%M %p')
    
    return df.drop(labels=['depart_time','destination','origin'],axis=1)
