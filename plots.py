import plotly.express as px


def create_scatterplot(df):
    """
    Creates a scatterplot for the given DataFrame.

    Args:
        df (pandas.DataFrame): Data frame containing columns 'GDP per capita', 'Healthy Life Expectancy (IHME)', and 'country'.

    Returns:
        plotly.graph_objects.Figure: Scatterplot figure object.

    Raises:
        ValueError: If required columns are missing from the DataFrame.
    """
    required_columns = ["GDP per capita", "Healthy Life Expectancy (IHME)", "country"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain '{col}' column")
    fig = px.scatter(
        df,
        x=required_columns[0],  # 'GDP per capita'
        y=required_columns[1],  # 'Healthy Life Expectancy (IHME)'
        hover_name=required_columns[2],
        size=required_columns[0],
        color=required_columns[2],
        title="Life Expectancy vs GDP per Capita",
        labels={
            "GDP per capita": "GDP per Capita (log scale)",
            "life_expectancy": "Life Expectancy (IHME)",
        },
        log_x=True,
        size_max=40,
        template="plotly_white",
    )

    fig.update_layout(legend_title_text="Country")

    return fig
