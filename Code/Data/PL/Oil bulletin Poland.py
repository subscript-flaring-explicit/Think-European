## import pandas as pd
import pandas as pd

# import plotly express as px
import plotly.express as px

## open excel .xlsx file in read mode as pandas dataframe:
df = pd.read_excel("/home/gr00stl/Documents/Projects/Publico/Dane/pl/Oil_Bulletin_Prices_History_PL.xlsx", thousands = ",", decimal = ".")

# convert date column to datetime:
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# sort dataframe by date, get last year:
last_year = df.loc[(df['Date'] >= '2021-06-01') & (df['Date'] <= '2022-06-07')]

# display last year:
print(last_year)

## add column with values of fourth column divided by values in third column: last_year['Euro-super 95'] / last_year['Euro-super 95']*1000 as last_year['Euro-super 95 (zł) za litr']
last_year['Euro-super 95 (zł) za litr'] = (last_year['Euro-super 95  (I)'] / 1000) / last_year['Exchange_x000D_Rate_x000D_To €']

# create a plot of last year of value in Euro-super 95: last_year.iloc[:,2]
# plt.plot(last_year.iloc[:,2])

# order dataframe by date:
last_year.sort_values(by=['Date'], inplace=True, ascending=True)

# create a figure:
fig = px.line(last_year, x='Date', y='Euro-super 95 (zł) za litr', title='Cena litra benzyny 95-oktanowej w ciągu ostatniego roku w Polsce', labels = {"Date": "data"})

# px.line(last_year_95_order, x='Date', y='Euro-super 95  (I)', title='Cena Euro-super 95 w ciągu ostatniego roku w Polsce')

# change x axis title
fig.update_xaxes(title_text="Czas")

## add footer at the right bottom of plotly chart: fig.update_layout(annotations=[dict(xref='paper', yref='paper', x=1, y=1, xanchor='right', yanchor='bottom', text='Data z dnia 24 lutego 2020r.', font_size=12, showarrow=False)])
fig.update_layout(annotations=[dict(x=1, y=0, showarrow=False, text="Źródło danych: Weekly Oil Bulletin - UE<br>opracowanie: thinkeuropean.org", xref="paper", yref="paper", xanchor='right', yanchor='bottom')])

# add vertical line to plotly chart:
# fig.add_vline(x = "2022-02-24")
fig.add_vrect(x0="2022-02-24", x1="2022-06-06", annotation_text="Agresja rosyjska", annotation_position="top left", fillcolor="red", opacity=0.25, line_width=0)

## add custom logo: 
fig.add_layout_image(
  dict(
      source="https://raw.githubusercontent.com/subscript-flaring-explicit/Think-European/main/Logos/Think%20European%20-%20chart%20logo.svg",
      xref="paper", yref="paper",
      x=1, y=1.1,
      sizex=0.05, sizey=0.05,
      xanchor="right", yanchor="top"
  )
)

## export to html smaller size:
# export to html - smaller size
with open('/home/gr00stl/Documents/Git/Think-European/Think-European/Data/PL/Cena benzyny 95.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))


# show figure: fig.show()
fig.show()