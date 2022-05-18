import feather
import numpy as np
import pandas as pd
import timeit

def create_df():
    size = 10000000
    df = pd.DataFrame({
        'a': np.random.rand(size),
        'b': np.random.rand(size),
        'c': np.random.rand(size),
        'd': np.random.rand(size)
    })
    return df

def save_to_feather(df):
    df.to_feather('files/large.feather')

def save_to_csv(df):
    df.to_csv("files/large.csv")

def read_feather():
    df = pd.read_feather('files/large.feather')
    return df

def read_csv():
    df = pd.read_csv('files/large.csv')
    return df

duration_feather = 0
duration_csv = 0
duration_read_feather = 0
duration_read_csv = 0
runs = 1000
for i in range(runs):
    df = create_df()
    start = timeit.default_timer()
    save_to_feather(df)
    duration_feather += timeit.default_timer() - start

    start = timeit.default_timer()
    save_to_csv(df)
    duration_csv += timeit.default_timer() - start

    start = timeit.default_timer()
    df = read_feather()
    duration_read_feather += timeit.default_timer() - start

    start = timeit.default_timer()
    df2 = read_csv()
    duration_read_csv += timeit.default_timer() - start

    print(f"Current stats for writing feather:  {duration_feather / (i+1)}")
    print(f"Current stats for writing csv:  {duration_csv / (i+1)}")
    print(f"Current stats for reading feather:  {duration_read_feather / (i+1)}")
    print(f"Current stats for reading csv:  {duration_read_csv / (i+1)}")

print(duration_feather / runs)
print(duration_csv / runs)
print(duration_read_feather / runs)
print(duration_read_csv / runs)
