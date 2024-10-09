import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Hasil Pertanian",
    page_icon="🌴",
)

#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 100)
t2.title("Desa Cibiru Wetan")
t2.markdown(" **Halaman Data Hasil Pertanian dan Perkebunan Desa Cibiru Wetan, Cileunyi, Kab. Bandung** ")
st.write(" **Tahun 2023** ")

url10='https://docs.google.com/spreadsheets/d/15sfFQbVZUmseAfOv70EXI4pe3wUusL9OvfeOex43ueg/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
pt23 = conn.read(spreadsheet=url10)
pt23 = pd.DataFrame(pt23)                       #convert ke panda df
lahan23 = pt23.iloc[68:73,0:2]
lahan23.index = list(lahan23.iloc[0:3,0])
lahan23 = lahan23.iloc[0:3,1:2]
pt23 = pt23.iloc[0:65,0:4]
pt23.index = list(pt23.iloc[0:65,0])
pt23 = pt23.iloc[0:65,1:4]

import altair as alt
st.write('# Luas Lahan Pertanian dan Perkebunan Berdasarkan Jenis Produksi')
data = pd.melt(lahan23.reset_index(), id_vars=["index"])
chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)
st.altair_chart(chart, use_container_width=True)   

chart = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="index", type="nominal"),
)
st.altair_chart(chart, use_container_width=True)  

st.write('## Tanaman Pangan Berdasarkan Komoditas')
datatp1 = pt23.iloc[0:31,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Luas Lahan (Ha)', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text1 = charttp1.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp1 = (charttp1 + text1)
datatp2 = pt23.iloc[0:31,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Hasil Panen (Ton/Ha)', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text2 = charttp2.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp2 = (charttp2 + text2)
tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

st.write('## Tanaman Buah-buahan Berdasarkan Komoditas')
datatp1 = pt23.iloc[31:58,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Luas Lahan (Ha)', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text1 = charttp1.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp1 = (charttp1 + text1)
datatp2 = pt23.iloc[31:58,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Hasil Panen (Ton/Ha)', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text2 = charttp2.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp2 = (charttp2 + text2)
tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)  

st.write('## Perkebunan Berdasarkan Komoditas')
datatp1 = pt23.iloc[58:65,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Luas Lahan (Ha)', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text1 = charttp1.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp1 = (charttp1 + text1)
datatp2 = pt23.iloc[58:65,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Hasil Panen (Ton/Ha)', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text2 = charttp2.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp2 = (charttp2 + text2)
tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)  

st.write('# Tabel Luas Lahan Hasil Pertanian dan Perkebunan')
st.dataframe(pt23,use_container_width=True)

with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Data Hasil Pertanian Desa Cibiru Wetan")
    st.caption("""Data hasil pertanian menyediakan data luas lahan serta hasil panen dari berbagai komoditas tanaman pangan, buah-buahan, dan hasil perkebunan di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
