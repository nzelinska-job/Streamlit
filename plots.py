import plotly.express as px

def create_scatterplot(df):
    """
    Creates a scatterplot for the filtered data frame.
    
    Input:
    df : pandas.DataFrame - 'gdp_per_capita', 'life_expectancy', 'country'

    Return:
    fig : plotly.graph_objects.Figure - Scatterplot of life expectancy vs GDP per capita
    """

    required_columns = ['GDP per capita', 'Healthy Life Expectancy (IHME)', 'country']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame should contain '{col}'")

    fig = px.scatter(
        df,
        x=required_columns[0],  # 'GDP per capita'
        y=required_columns[1],  # 'Healthy Life Expectancy (IHME)'
        hover_name=required_columns[2],
        size=required_columns[0],
        color=required_columns[2],
        title='Life Expectancy vs GDP per Capita',
        labels={
            'GDP per capita': 'GDP per Capita (log scale)',
            'life_expectancy': 'Life Expectancy (IHME)'
        },
        log_x=True,
        size_max=40,
        template='plotly_white'
    )

    fig.update_layout(legend_title_text='Country')

    return fig
