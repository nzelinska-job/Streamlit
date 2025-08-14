import streamlit as st
from utils import first_function
from config import DATA_URL
import pandas as pd
from plots import create_scatterplot

st.title("Worldwide Analysis of Quality of Life and Economic Factors")

st.subheader("This app enables you to explore the relationships between poverty, life expectancy, and GDP across various countries and years. Use the panels to select options and interact with the data.", width="stretch")

df = pd.read_csv(DATA_URL)
min_year = int(df['year'].min())
max_year = int(df['year'].max())

tab1, tab2, tab3 = st.tabs(["CatGlobal Overview", "Country Deep Dive", "Data Explorer"], width="stretch")



with tab1:
    st.header("Global Overview")

    selected_year = st.slider(
        "Select the year:",
        min_value=min_year,
        max_value=max_year,
        value=min_year,
        step=1)

    df_year = df[df['year'] == selected_year]

    mean_life_exp = df_year['Healthy Life Expectancy (IHME)'].mean()
    median_gdp = df_year['GDP per capita'].median()
    mean_pov_rate = df_year['headcount_upper_mid_income_povline'].mean()
    num_countries = df_year['country'].nunique()

    col1, col2, col3, col4 = st.columns(4, width="stretch")

    col1.metric(
        label="📈 Mean Life Expectancy",
        value=f"{mean_life_exp:.2f}",
        delta=None
    )
    
    col2.metric(
        label="💰 Median GDP per Capita",
        value=f"{median_gdp:,.0f}",
        delta=None
    )
    
    col3.metric(
        label="📉 Mean Upper-Mid Income Poverty Ratio",
        value=f"{mean_pov_rate:.2f}",
        delta=None
    )

    col4.metric(
        label="🌍 Number of countries with data for the selected year",
        value=num_countries,
        delta=None
    )

    st.dataframe(df_year)

    fig = create_scatterplot(df_year)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Country Deep Dive")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Data Explorer")

    countries = df['country'].unique()

    selected_years = st.slider(
    "Select the year range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
    )

    selected_countries = st.multiselect(
        "Countries:",
        options=sorted(countries),
        default=sorted(countries)[-5:]  # Default to the last 5 countries
    )
    filtered_df = df[
        (df['country'].isin(selected_countries)) &
        (df['year'] >= selected_years[0]) &
        (df['year'] <= selected_years[1])
    ]

    st.dataframe(filtered_df)

    tab3.line_chart(filtered_df[['year', 'headcount_ratio_international_povline']].set_index('year'))

    st.download_button(
        label="Save as CSV",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_global_development_data.csv",
        mime="text/csv"
    )

st.balloons()
