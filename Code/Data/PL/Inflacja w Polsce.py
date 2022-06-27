import plotly.express as px
import pandas as pd
from dbnomics import fetch_series

## import deepl API
import deepl

# initialize deepl API
translator = deepl.Translator('5735d7e3-113a-8810-a9d6-dbb4a7e30cc2:fx')

# result = translator.translate_text("{}".format(), target_lang="EN-US")

# print(result)

dfs = []

# Poland – Consumer Price Index > Food and non-Alcoholic beverages (COICOP 01) > Total > Total – Contribution to annual inflation – Monthly
df1 = fetch_series("OECD/MEI/POL.CP010000.CTGY.M")
df1["series_id"] = df1["series_name"].str.split(">").str[1]
dfs.append(df1)
# # display(df1)
# display(px.line(df1, x="period", y="value", title=df1.series_id[0]))

# Poland – Consumer Price Index > Clothing and footwear (COICOP 03) > Total > Total – Contribution to annual inflation – Monthly
df2 = fetch_series("OECD/MEI/POL.CP030000.CTGY.M")
df2["series_id"] = df2["series_name"].str.split(">").str[1]
dfs.append(df2)
# # display(df2)
# display(px.line(df2, x="period", y="value", title=df2.series_id[0]))

# Poland – Consumer Price Index > Housing, water, electricity, gas and other fuels (COICOP 04) > Total > Total – Contribution to annual inflation – Monthly
df3 = fetch_series("OECD/MEI/POL.CP040000.CTGY.M")
df3["series_id"] = df3["series_name"].str.split(">").str[1]
dfs.append(df3)
# # display(df3)
# display(px.line(df3, x="period", y="value", title=df3.series_id[0]))

# Poland – Consumer Price Index > Furnishings, household equip. and routine household maintenance (COICOP 05) > Total > Total – Contribution to annual inflation – Monthly
df4 = fetch_series("OECD/MEI/POL.CP050000.CTGY.M")
df4["series_id"] = df4["series_name"].str.split(">").str[1]
dfs.append(df4)
# # display(df4)
# display(px.line(df4, x="period", y="value", title=df4.series_id[0]))

# Poland – Consumer Price Index > Health (COICOP 06) > Total > Total – Contribution to annual inflation – Monthly
df5 = fetch_series("OECD/MEI/POL.CP060000.CTGY.M")
df5["series_id"] = df5["series_name"].str.split(">").str[1]
dfs.append(df5)
# # display(df5)
# display(px.line(df5, x="period", y="value", title=df5.series_id[0]))

# Poland – Consumer Price Index > Alcoholic beverages, tobacco and narcotics (COICOP 02) > Total > Total – Contribution to annual inflation – Monthly
df6 = fetch_series("OECD/MEI/POL.CP020000.CTGY.M")
df6["series_id"] = df6["series_name"].str.split(">").str[1]
dfs.append(df6)
# # display(df6)
# display(px.line(df6, x="period", y="value", title=df6.series_id[0]))

# Poland – Consumer Price Index > Transport (COICOP 07) > Total > Total – Contribution to annual inflation – Monthly
df7 = fetch_series("OECD/MEI/POL.CP070000.CTGY.M")
df7["series_id"] = df7["series_name"].str.split(">").str[1]
dfs.append(df7)
# # display(df7)
# display(px.line(df7, x="period", y="value", title=df7.series_id[0]))

# Poland – Consumer Price Index > Communication (COICOP 08) > Total > Total – Contribution to annual inflation – Monthly
df8 = fetch_series("OECD/MEI/POL.CP080000.CTGY.M")
df8["series_id"] = df8["series_name"].str.split(">").str[1]
dfs.append(df8)
# # display(df8)
# display(px.line(df8, x="period", y="value", title=df8.series_id[0]))

# Poland – Consumer Price Index > Recreation and culture  (COICOP 09) > Total > Total – Contribution to annual inflation – Monthly
df9 = fetch_series("OECD/MEI/POL.CP090000.CTGY.M")
df9["series_id"] = df9["series_name"].str.split(">").str[1]
dfs.append(df9)
# # display(df9)
# display(px.line(df9, x="period", y="value", title=df9.series_id[0]))

# Poland – Consumer Price Index > Education (COICOP 10) > Total > Total – Contribution to annual inflation – Monthly
df10 = fetch_series("OECD/MEI/POL.CP100000.CTGY.M")
df10["series_id"] = df10["series_name"].str.split(">").str[1]
dfs.append(df10)
# # display(df10)
# display(px.line(df10, x="period", y="value", title=df10.series_id[0]))

# Poland – Consumer Price Index > Restaurants and hotels (COICOP 11) > Total > Total – Contribution to annual inflation – Monthly
df11 = fetch_series("OECD/MEI/POL.CP110000.CTGY.M")
df11["series_id"] = df11["series_name"].str.split(">").str[1]
dfs.append(df11)
# # display(df11)
# display(px.line(df11, x="period", y="value", title=df11.series_id[0]))

# Poland – Consumer Price Index > All items > Total > Total – Contribution to annual inflation – Monthly
# df12 = fetch_series("OECD/MEI/POL.CPALTT01.CTGY.M")
# df12["series_id"] = df12["series_name"].str.split(">").str[1]
# dfs.append(df12)
# # display(df12)
# display(px.line(df12, x="period", y="value", title=df12.series_id[0]))

df_all = pd.concat(dfs)

# df_all['series_id'] = 

# for i in df_all.series_id:
#     translator.translate_text(i, target_lang="pl")

# change values of series_id to polish: df_all.series_id = df_all.series_id.apply(translator.translate_text, target_lang="pl")
# df_all.series_id = df_all.series_id.apply(translator.translate_text, target_lang="pl")

# change 

print(df_all.head())

## get labels from translator: deepl.translate(df_all.series_id.unique(), target_lang="pl")
df_all['series_id_pl'] = translator.translate_text(df_all.series_id, target_lang="pl")
df_all['series_id'] = df_all.series_id_pl.apply(lambda x: x.text)

fig = px.line(df_all, x="period", y="value", color="series_id", title="Co wpływa na inflację w Polsce", template = 'seaborn', labels= {"series_id": "Kategoria", "value": "Wartość", "period": "Czas"})

## change figure colors: fig.update_traces(marker=dict(color=df_all.series_id))
# fig.update_traces(marker=dict(color=df_all.series_id_pl))

print(df_all)

## change x axis and y axis labels: 
fig.update_xaxes(title_text="Czas")
fig.update_yaxes(title_text="Wpływ na inflację w punktach %")

## change hoverbox template: fig.update_layout(template="plotly_dark")
# fig.update_traces(hovertemplate="%{y:.2f}%")

fig.update_layout(legend_title = "Składnik inflacji")

## change legend position to left upper corner: 
fig.update_layout(legend=dict(x=0, y=1))

## add footer at the top right text with source: 
fig.update_layout(annotations=[dict(x=1, y=0, showarrow=False, text="Źródło danych: OECD<br>opracowanie: <a href=”https://thinkeuropean.org/”>Think European</a>", xref="paper", yref="paper", align = "right")])


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
with open('/home/gr00stl/Documents/Git/Think-European/Think-European/Data/PL/Składniki inflacji w Polsce.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))

fig.show()