import pandas as pd

def update_time(df): 
    new_time = pd.to_datetime(df['sched_time'], format='%I:%M %p') + pd.to_timedelta(df['late'], unit='m')
    df.loc[:, 'estimated_time'] = new_time
    df['estimated_time'] = pd.to_datetime(df['estimated_time'], format='%I:%M%p')
    df['estimated_time'] = df['estimated_time'].dt.strftime('%I:%M%p')
    return df

def process_dataframe(current_df, status_df):
    merged_df = pd.merge(current_df, status_df, on='train_id', how='left')
    needs_update_df = merged_df[(merged_df['late'] > 0)].drop(['day', 'line', 'direction', 'path', 'service_type'], axis=1)
    updated = update_time(needs_update_df)
    updated.loc[:, 'status'] = needs_update_df['late'].astype(int).astype(str) + ' min'
    updated_df = updated.drop(['late', 'sched_time'], axis=1)
    final_df = update_initial_dataframe(current_df, updated_df)
    return final_df

def update_initial_dataframe(initial_df, processed_df):
    processed_df.set_index(['train_id', 'date'], inplace=True)
    initial_df.set_index(['train_id', 'date'], inplace=True)
    initial_df.update(processed_df)
    initial_df.reset_index(inplace=True)
    return initial_df
