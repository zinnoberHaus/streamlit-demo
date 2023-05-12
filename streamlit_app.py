# import streamlit as st
# import plotly.express as px
# import pandas as pd
# from streamlit_plotly_events import plotly_events
# import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]

# df=[]
# df= pd.DataFrame(df)
# df['year']= x
# df['lifeExp']= y

# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

# selected_points = plotly_events(fig)
# selected_points
# a=selected_points[0]

# df = pd.DataFrame(
#    np.random.randn(50, 20),
#    columns=('col %d' % i for i in range(20)))

# st.dataframe(df)  # Same as st.write(df)
# # df
# # a= pd.DataFrame.from_dict(a,orient='index')
# # a


# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])
df
# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")