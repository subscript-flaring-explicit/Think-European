import plotly.express as px
import pandas as pd
from dbnomics import fetch_series

# import datetime as dt
import datetime as dt

from xarray import align

# import deepl
import deepl

## initialize deepl API
translator = deepl.Translator('ef10af44-f658-5c9d-f3b0-0c1e0f4b2e6c:fx')

dfs = []

# Austria – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df1 = fetch_series("OECD/MEI/AUT.CPALTT01.CTGY.M")
df1["series_id"] = df1['Country']

# print(df1['Country'])

# get country name from country code: 
# df1['Country'] 

dfs.append(df1)
# #display(df1)
#display(px.line(df1, x="period", y="value", title=df1.series_id[0]))

# Belgium – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df2 = fetch_series("OECD/MEI/BEL.CPALTT01.CTGY.M")
df2["series_id"] = df2['Country']
dfs.append(df2)
# #display(df2)
#display(px.line(df2, x="period", y="value", title=df2.series_id[0]))

# Switzerland – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df3 = fetch_series("OECD/MEI/CHE.CPALTT01.CTGY.M")
df3["series_id"] = df3['Country']
dfs.append(df3)
# #display(df3)
#display(px.line(df3, x="period", y="value", title=df3.series_id[0]))

# Czech Republic – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df4 = fetch_series("OECD/MEI/CZE.CPALTT01.CTGY.M")
df4["series_id"] = df4['Country']
dfs.append(df4)
# #display(df4)
#display(px.line(df4, x="period", y="value", title=df4.series_id[0]))

# Germany – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df5 = fetch_series("OECD/MEI/DEU.CPALTT01.CTGY.M")
df5["series_id"] = df5['Country']
dfs.append(df5)
# #display(df5)
#display(px.line(df5, x="period", y="value", title=df5.series_id[0]))

# Denmark – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df6 = fetch_series("OECD/MEI/DNK.CPALTT01.CTGY.M")
df6["series_id"] = df6['Country']
dfs.append(df6)
# #display(df6)
#display(px.line(df6, x="period", y="value", title=df6.series_id[0]))

# Spain – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df7 = fetch_series("OECD/MEI/ESP.CPALTT01.CTGY.M")
df7["series_id"] = df7['Country']
dfs.append(df7)
# #display(df7)
#display(px.line(df7, x="period", y="value", title=df7.series_id[0]))

# Estonia – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df8 = fetch_series("OECD/MEI/EST.CPALTT01.CTGY.M")
df8["series_id"] = df8['Country']
dfs.append(df8)
# #display(df8)
#display(px.line(df8, x="period", y="value", title=df8.series_id[0]))

# Finland – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df9 = fetch_series("OECD/MEI/FIN.CPALTT01.CTGY.M")
df9["series_id"] = df9['Country']
dfs.append(df9)
# #display(df9)
#display(px.line(df9, x="period", y="value", title=df9.series_id[0]))

# France – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df10 = fetch_series("OECD/MEI/FRA.CPALTT01.CTGY.M")
df10["series_id"] = df10['Country']
dfs.append(df10)
# #display(df10)
#display(px.line(df10, x="period", y="value", title=df10.series_id[0]))

# United Kingdom – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df11 = fetch_series("OECD/MEI/GBR.CPALTT01.CTGY.M")
df11["series_id"] = df11['Country']
dfs.append(df11)
# #display(df11)
#display(px.line(df11, x="period", y="value", title=df11.series_id[0]))

# Greece – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df12 = fetch_series("OECD/MEI/GRC.CPALTT01.CTGY.M")
df12["series_id"] = df12['Country']
dfs.append(df12)
# #display(df12)
#display(px.line(df12, x="period", y="value", title=df12.series_id[0]))

# Hungary – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df13 = fetch_series("OECD/MEI/HUN.CPALTT01.CTGY.M")
df13["series_id"] = df13['Country']
dfs.append(df13)
# #display(df13)
#display(px.line(df13, x="period", y="value", title=df13.series_id[0]))

# Ireland – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df14 = fetch_series("OECD/MEI/IRL.CPALTT01.CTGY.M")
df14["series_id"] = df14['Country']
dfs.append(df14)
# #display(df14)
#display(px.line(df14, x="period", y="value", title=df14.series_id[0]))

# Iceland – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df15 = fetch_series("OECD/MEI/ISL.CPALTT01.CTGY.M")
df15["series_id"] = df15['Country']
dfs.append(df15)
# #display(df15)
#display(px.line(df15, x="period", y="value", title=df15.series_id[0]))

# Italy – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df16 = fetch_series("OECD/MEI/ITA.CPALTT01.CTGY.M")
df16["series_id"] = df16['Country']
dfs.append(df16)
# #display(df16)
#display(px.line(df16, x="period", y="value", title=df16.series_id[0]))

# Lithuania – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df17 = fetch_series("OECD/MEI/LTU.CPALTT01.CTGY.M")
df17["series_id"] = df17['Country']
dfs.append(df17)
# #display(df17)
#display(px.line(df17, x="period", y="value", title=df17.series_id[0]))

# Luxembourg – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df18 = fetch_series("OECD/MEI/LUX.CPALTT01.CTGY.M")
df18["series_id"] = df18['Country']
dfs.append(df18)
# #display(df18)
#display(px.line(df18, x="period", y="value", title=df18.series_id[0]))

# Latvia – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df19 = fetch_series("OECD/MEI/LVA.CPALTT01.CTGY.M")
df19["series_id"] = df19['Country']
dfs.append(df19)
# #display(df19)
#display(px.line(df19, x="period", y="value", title=df19.series_id[0]))

# Netherlands – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df20 = fetch_series("OECD/MEI/NLD.CPALTT01.CTGY.M")
df20["series_id"] = df20['Country']
dfs.append(df20)
# #display(df20)
#display(px.line(df20, x="period", y="value", title=df20.series_id[0]))

# Norway – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df21 = fetch_series("OECD/MEI/NOR.CPALTT01.CTGY.M")
df21["series_id"] = df21['Country']
dfs.append(df21)
# #display(df21)
#display(px.line(df21, x="period", y="value", title=df21.series_id[0]))

# Poland – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df22 = fetch_series("OECD/MEI/POL.CPALTT01.CTGY.M")
df22["series_id"] = df22['Country']
dfs.append(df22)
# #display(df22)
#display(px.line(df22, x="period", y="value", title=df22.series_id[0]))

# Portugal – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df23 = fetch_series("OECD/MEI/PRT.CPALTT01.CTGY.M")
df23["series_id"] = df23['Country']
dfs.append(df23)
# #display(df23)
#display(px.line(df23, x="period", y="value", title=df23.series_id[0]))

# Slovak Republic – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df24 = fetch_series("OECD/MEI/SVK.CPALTT01.CTGY.M")
df24["series_id"] = df24['Country']
dfs.append(df24)
# #display(df24)
#display(px.line(df24, x="period", y="value", title=df24.series_id[0]))

# Slovenia – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df25 = fetch_series("OECD/MEI/SVN.CPALTT01.CTGY.M")
df25["series_id"] = df25['Country']
dfs.append(df25)
# #display(df25)
#display(px.line(df25, x="period", y="value", title=df25.series_id[0]))

# Sweden – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df26 = fetch_series("OECD/MEI/SWE.CPALTT01.CTGY.M")
df26["series_id"] = df26['Country']
dfs.append(df26)
# #display(df26)
#display(px.line(df26, x="period", y="value", title=df26.series_id[0]))

# Turkey – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
df27 = fetch_series("OECD/MEI/TUR.CPALTT01.CTGY.M")
df27["series_id"] = df27['Country']
dfs.append(df27)
# #display(df27)
#display(px.line(df27, x="period", y="value", title=df27.series_id[0]))

df_all = pd.concat(dfs)

# country_list = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Slovak Republic', 'Slovenia', 'Sweden', 'Turkey']

# change series id values to country_list: df_all['series_id'] = df_all['series_id'].replace(country_list)
# df_all['series_id'] = df_all['series_id'].replace(country_list)

# translate series_id to polish: df_all['series_id'] = translator.translate_text(df_all.series_id, target_language='pl')
df_all['series_id'] = translator.translate_text(df_all.series_id, target_lang='pl', formality= 'less')
df_all['series_id'] = df_all.series_id.apply(lambda x: x.text)

# order series_id alphabetically: df_all.sort_values(by=['series_id'], inplace=True, ascending=True)
df_all.sort_values(by=['series_id'], ascending=True)

# create figure for all countries
fig = px.line(df_all, x="period", y="value", color="series_id", title="Inflacja w wybranych krajach Europy")

## change x axis label to Czas: fig.update_xaxes(title_text="Czas")
fig.update_xaxes(title_text="Czas")

## change y axis label to Wartość inflacji (%): fig.update_yaxes(title_text="Wartość inflacji (%)")
fig.update_yaxes(title_text="Wartość inflacji (%)")

# fig.update_layout(legend={"xanchor": "right", "yanchor": "bottom"})

## change x value range to start in year 2010: fig.update_xaxes(range=[2010, 2022])
## print x axis values: print(fig.data[0]['x'])
print(fig.data[0]['x'])

## start x axis in datetime year 2010: fig.update_xaxes(type="date", range=[datetime.datetime(2010, 1, 1, 0, 0), datetime.datetime(2022, 5, 1, 0, 0))])
fig.update_xaxes(type="date", range=[dt.datetime(2010, 1, 1, 0, 0), dt.datetime(2022, 5, 1, 0, 0)])

# change legend position to left bottom: fig.update_layout(legend={"xanchor": "left", "yanchor": "bottom"})
fig.update_layout(legend={"x": 0, "y": -0.1, "orientation": "h"})

## change legend title to "Kraj": fig.update_layout(legend_title_text="Kraj")
fig.update_layout(legend_title_text="Kraj")

## add footer at the right bottom of plotly chart: fig.update_layout(annotations=[dict(xref='paper', yref='paper', x=1, y=1, xanchor='right', yanchor='bottom', text='Data z dnia 24 lutego 2020r.', font_size=12, showarrow=False)])
fig.update_layout(annotations=[dict(x=1, y=0, showarrow=False, text="Źródło danych: OECD<br>opracowanie: <a href=”https://thinkeuropean.org/”>Think European</a>", xref="paper", yref="paper", xanchor='right', yanchor='bottom', align = 'right')])

## add custom logo: 
fig.add_layout_image(
  dict(
      source="https://raw.githubusercontent.com/subscript-flaring-explicit/Think-European/main/Logos/Think%20European%20-%20chart%20logo.svg",
      xref="paper", yref="paper",
      x=1, y=1.05,
      sizex=0.05, sizey=0.05,
      xanchor="center", yanchor="middle"
  )
)

# show plot: fig.show()
fig.show()

# save figure to html with minified size: fig.write_html("inflacja_europy.html", include_plotlyjs="cdn")
fig.write_html("/home/gr00stl/Documents/Git/Think-European/Think-European/Data/EU/Inflacja w krajach Europy.html", include_plotlyjs="cdn")