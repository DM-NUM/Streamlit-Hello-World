import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses: :happly:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

fig, ax = plt.subplots(1, figsize=(8,6))
ax.scatter(df2['a'], df2['b'])
ax.set_title('hellow world')
ax.set_xlabel('hha')
st.write(fig)


st.header('test markdown')
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')

st.header('大标题')
st.subheader('子标题')
st.caption("加入一些说明，小字体")

st.write(df2)


st.header('test plotly')
import plotly.graph_objs as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=df2['a'], y=df2['b'], mode='markers', name='test'))
# fig.update_traces(marker_color='rgb(15,110,225)', # marker颜色
#                   marker_line_color='rgb(108,48,107)', # 线条颜色
#                   marker_line_width=1.5,   # 线宽
#                   opacity=0.6) 
# fig.show()
st.write(fig)