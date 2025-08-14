import streamlit as st
import pandas as pd

st.title("Worldwide Analysis of Quality of Life and Economic Factors")

st.subheader("This app enables you to explore the relationships between poverty, life expectancy, and GDP across various countries and years. Use the panels to select options and interact with the data.", width="stretch")
# st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"], width="stretch")

DATA_URL = 'https://raw.githubusercontent.com/JohannaViktor/streamlit_practical/refs/heads/main/global_development_data.csv'
df = pd.read_csv(DATA_URL)

tab1, tab2, tab3 = st.tabs(["CatGlobal Overview", "Country Deep Dive", "Data Explorer"], width="stretch")

with tab1:
    st.header("Global Overview")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("Country Deep Dive")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Data Explorer")

    countries = df['country'].unique()
    selected_countries = st.multiselect(
        "Countries:",
        options=sorted(countries),
        default=sorted(countries)[:5]
    )
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    selected_years = st.slider(
        "Select the year range:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    filtered_df = df[
        (df['country'].isin(selected_countries)) &
        (df['year'] >= selected_years[0]) &
        (df['year'] <= selected_years[1])
    ]

    st.dataframe(filtered_df)

    st.download_button(
        label="Save as CSV",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_global_development_data.csv",
        mime="text/csv"
    )







st.button("Click Me", on_click=lambda: st.write("Button clicked!")) 
st.text_input("Enter some text", placeholder="Type here...")
st.slider("Select a number", 0, 100, 50)
st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.checkbox("Check me out")
st.radio("Pick one", ["Choice A", "Choice B", "Choice C"])
st.text_area("Write something here", height=100)
st.file_uploader("Upload a file", type=["txt", "csv"])
st.image("https://via.placeholder.com/150", caption="Sample Image")
st.video("https://www.w3schools.com/html/mov_bbb.mp4", caption  ="Sample Video")
st.markdown("## Markdown Example")
st.markdown("""
This is an example of **Markdown** syntax in Streamlit.
- Bullet point 1
- Bullet point 2
```python
def hello_world():
    print("Hello, world!")
```
""")
st.json({"key": "value", "number": 42, "boolean": True})
st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
st.table({"Column A": [         "Row 1", "Row 2", "Row 3"],
          "Column B": [10, 20, 30]})
st.progress(50)
st.spinner("Loading... Please wait.")
st.balloons()
st.sidebar.title("Sidebar Example")
st.sidebar.write("This is a sidebar in Streamlit.")
st.sidebar.button("Sidebar Button", on_click=lambda: st.sidebar.write("Sidebar button clicked!"))
st.sidebar.selectbox("Sidebar Selectbox", ["Item 1", "Item 2", "Item 3"])
st.sidebar.slider("Sidebar Slider", 0, 100, 25)
st.sidebar.checkbox("Sidebar Checkbox")
st.sidebar.radio("Sidebar Radio", ["Option X", "Option Y", "Option Z"])
st.sidebar.text_input("Sidebar Text Input", placeholder="Type here...")
st.sidebar.text_area("Sidebar Text Area", height=100)
st.sidebar.file_uploader("Sidebar File Uploader", type=["jpg", "png"])
st.sidebar.image("https://via.placeholder.com/100", caption="Sidebar Image")
st.sidebar.video("https://www.w3schools.com/html/mov_bbb.mp4", caption="Sidebar Video")
st.sidebar.markdown("### Sidebar Markdown Example")