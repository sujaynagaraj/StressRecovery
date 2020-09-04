import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import fitparse

path = "COVID Stress _ Recovery - Sample Data/oura/"

activity = pd.read_parquet(path+"oura_activity/participant_id=U-ZR22B6HNLFMQ9FG6UR6Y/"+"62a20e3762154ed8a82fb00e355e95c1.parquet")

readiness = pd.read_parquet(path+"oura_readiness/participant_id=U-ZR22B6HNLFMQ9FG6UR6Y/"+"e8410b4ab5d14a58bf3bd262cf4cf50e.parquet")

sleep = pd.read_parquet(path+"oura_sleep/participant_id=U-ZR22B6HNLFMQ9FG6UR6Y/"+"94f4cf0412fe47159d7f32036dca2ddd.parquet")

print(activity.head())

print(readiness.head())

print(sleep.head())