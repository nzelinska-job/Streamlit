import streamlit as st
from github import Github
from io import StringIO
from utils import first_function
from config import DATA_URL
import pandas as pd
from plots import create_scatterplot
from model import get_feature_importance
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import joblib

st.markdown(
    "<h1 style='text-align: center;'>Worldwide Analysis of Quality of Life and Economic Factors</h1>",
    unsafe_allow_html=True,
)
st.set_page_config(
    page_title="Cool App by nzelinska",
    page_icon="👾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "mailto:zelinska.nataliia.job@gmail.com",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


st.subheader(
    "This app enables you to explore the relationships between poverty, life expectancy, and GDP across various countries and years. Use the panels to select options and interact with the data.",
    width="stretch",
)

df = pd.read_csv(DATA_URL)
min_year = int(df["year"].min())
max_year = int(df["year"].max())

tab1, tab2, tab3 = st.tabs(
    ["CatGlobal Overview", "Country Deep Dive", "Data Explorer"], width="stretch"
)


with tab1:
    st.header("Global Overview")

    selected_year = st.slider(
        "Select the year:",
        min_value=min_year,
        max_value=max_year,
        value=min_year,
        step=1,
    )

    df_year = df[df["year"] == selected_year]

    mean_life_exp = df_year["Healthy Life Expectancy (IHME)"].mean()
    median_gdp = df_year["GDP per capita"].median()
    mean_pov_rate = df_year["headcount_upper_mid_income_povline"].mean()
    num_countries = df_year["country"].nunique()

    col1, col2, col3, col4 = st.columns(4, width="stretch")

    col1.metric(
        label="📈 Mean Life Expectancy", value=f"{mean_life_exp:.2f}", delta=None
    )

    col2.metric(
        label="💰 Median GDP per Capita", value=f"{median_gdp:,.0f}", delta=None
    )

    col3.metric(
        label="📉 Mean Upper-Mid Income Poverty Ratio",
        value=f"{mean_pov_rate:.2f}",
        delta=None,
    )

    col4.metric(
        label="🌍 Number of countries with data for the selected year",
        value=num_countries,
        delta=None,
    )

    st.dataframe(df_year)

    fig = create_scatterplot(df_year)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Country Deep Dive")
    countries = sorted(df["country"].unique())
    selected_countries = st.multiselect(
        "Pick a country:", countries, default=countries[:3]
    )

    # Фільтруємо датасет за вибраними країнами
    filtered_df = df[df["country"].isin(selected_countries)]

    if filtered_df.empty:
        st.warning("Please select at least one country to visualize data.")
    else:
        fig = go.Figure()
        for country in selected_countries:
            country_df = filtered_df[filtered_df["country"] == country]
            fig.add_trace(
                go.Scatter(
                    x=country_df["year"],
                    y=country_df["Healthy Life Expectancy (IHME)"],
                    mode="lines+markers",
                    name=f"Life Expectancy - {country}",
                    yaxis="y1",
                )
            )

        for country in selected_countries:
            country_df = filtered_df[filtered_df["country"] == country]
            fig.add_trace(
                go.Scatter(
                    x=country_df["year"],
                    y=country_df["GDP per capita"],
                    mode="lines+markers",
                    name=f"GDP per Capita - {country}",
                    yaxis="y2",
                    line=dict(dash="dot"),  # Для візуального розрізнення ліній
                )
            )

        # Налаштовуємо осі
        fig.update_layout(
            title="Life Expectancy and GDP per Capita Over Years",
            xaxis=dict(title="Year"),
            yaxis=dict(
                title="Life Expectancy", side="left", showgrid=False, zeroline=False
            ),
            yaxis2=dict(
                title="GDP per Capita",
                side="right",
                overlaying="y",
                showgrid=False,
                zeroline=False,
            ),
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
            ),
            height=600,
            template="plotly_white",
        )

        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Data Explorer")

    countries = df["country"].unique()

    selected_years = st.slider(
        "Select the year range:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
    )

    selected_countries = st.multiselect(
        "Countries:",
        options=sorted(countries),
        default=sorted(countries)[-5:],  # Default to the last 5 countries
    )
    filtered_df = df[
        (df["country"].isin(selected_countries))
        & (df["year"] >= selected_years[0])
        & (df["year"] <= selected_years[1])
    ]

    # df = st.dataframe(filtered_df)
    edited_df = st.data_editor(filtered_df)

    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
    st.write("Outside the form")


# Model training and prediction
model = joblib.load("rf_model.pkl")

gdp_min, gdp_max = float(df["GDP per capita"].min()), float(df["GDP per capita"].max())
pov_min, pov_max = float(df["headcount_upper_mid_income_povline"].min()), float(
    df["headcount_upper_mid_income_povline"].max()
)
year_min, year_max = int(df["year"].min()), int(df["year"].max())

gdp_input = st.number_input(
    "GDP per capita", min_value=gdp_min, max_value=gdp_max, value=gdp_min
)
pov_input = st.number_input(
    "Headcount Ratio Upper Mid Income Povline",
    min_value=pov_min,
    max_value=pov_max,
    value=pov_min,
)
year_input = st.slider("Year", min_value=year_min, max_value=year_max, value=year_min)

# Prediction btn
if st.button("Predict Life Expectancy"):
    input_data = pd.DataFrame(
        {
            "GDP per capita": [gdp_input],
            "headcount_upper_mid_income_povline": [pov_input],
            "year": [year_input],
        }
    )
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Life Expectancy): {prediction:.2f}")

st.subheader("Feature Importance")

feature_importances = get_feature_importance(model)
names = list(feature_importances.keys())
values = list(feature_importances.values())

fig, ax = plt.subplots()
ax.barh(names, values, color="skyblue")
ax.set_xlabel("Importance")
ax.set_title("Feature Importance in RandomForestRegressor")

st.pyplot(fig)
