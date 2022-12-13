### Contents of pages/Colision_Range.py ###
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

st.title("Vehicle collisions")

# Read Data Frame
df = pd.read_csv('NYC.csv')

# Set up two variables: factor & event
factor = ['VEHICLE 1 FACTOR', 'VEHICLE 2 FACTOR', 'VEHICLE 3 FACTOR', 'VEHICLE 4 FACTOR', 'VEHICLE 5 FACTOR']
event = ['PERSONS INJURED', 'PEDESTRIANS INJURED', 'CYCLISTS INJURED', 'MOTORISTS INJURED']

# Create new column "Factors" and store the main factor
df['Factor'] = np.nan
for index, row in df.iterrows():
    for f in factor:
        if row[f] not in ['UNSPECIFIED', np.nan]:
            df.loc[index, 'Factor'] = row[f]
            break

# New filter: From the original dataframe, we create a "copy" dataframe (df_), ruling out the Nan in column "Factor" and re-setting index{1,2,3}
df_ = df[~df['Factor'].isna()]
df_.reset_index(drop=True, inplace=True)

# We create a new dataframe (df_factor)
# Use groupby. to sum the number of injured parties ("events" list) belonging to each factor.
df_factor = df_.groupby(['Factor'])[event].sum()

# Create a new column named "counts" in the dataframe. used the .size() to count the number of events.
df_factor['counts'] = df_.groupby(['Factor']).size()

# df_factors are ordered by descending value. The first 5 factors will be used.
df_factor = df_factor.reset_index().sort_values(by='counts', ascending=False).reset_index(drop=True)

#Final data_frame: We select the top five factors using .iloc [0:5]
df_factor = df_factor.iloc[0:5]

#We plot the chart using the final dataframe (df_factor)
#We use Matplotlib
fig, ax = plt.subplots()

n = len(df_factor.index)
x = np.arange(n)
width = 0.2

ax.bar(x - width, df_factor[event[0]], width=width, label=event[0])
ax.bar(x, df_factor[event[1]], width=width, label=event[1])
ax.bar(x+width, df_factor[event[2]], width=width, label=event[2])
ax.bar(x+width*2, df_factor[event[3]], width=width, label=event[3])

#ax.bar(x+width*3,df_factor[event[4]],width=width, label=event[4])

plt.xticks(x, df_factor['Factor'], rotation = 90)
plt.legend(loc='best')

ax.set_title(f'Main five factors', fontsize=12,
             loc='left', pad = 20)
fig.suptitle(f'Numbers of persons INJURED', y=1, fontsize=10)
plt.ylabel('Number persons INJURED')

st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(df_factor['Factor'], df_factor['counts'])

ax.set_title(f'Main five factors', fontsize=12,
             loc='left', pad = 20)
fig.suptitle(f'Numbers of Accidents', y=1, fontsize=10)

plt.xticks(x, df_factor['Factor'], rotation = 90)
plt.ylabel('Number accidents')

st.pyplot(fig)



