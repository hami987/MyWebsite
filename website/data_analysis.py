import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

figurestoshow = []
# Cleaning Data
def transportationDataVis(data_path):
    dataset = pd.read_csv(data_path)
    pd.set_option('display.max_columns', None)
    dataset = dataset.dropna(axis=0,how="all")
    dataset = dataset.drop_duplicates(subset=["Period and Financial year"], keep="first")

    # Long-to-wide conversion for plotting
    dataset = dataset.reset_index()
    dataset = pd.melt(dataset, id_vars='Period and Financial year', value_vars=['Bus journeys (m)', 'Underground journeys (m)', 'DLR Journeys (m)',"Tram Journeys (m)","Overground Journeys (m)","Emirates Airline Journeys (m)"])

    # Building Plots

    line_plot = px.line(dataset, x="Period and Financial year",y="value",color="variable",
                        title="Usage of transportation modes per Month",
                        labels={"value":"Passengers", "Period and Financial year":"Year / Month",
                                "variable":"Mode of Transportation"})#, barmode="group")
    line_plot.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    #line_plot.show()
    figurestoshow.append(line_plot)

    pie_chart = px.pie(dataset,names="variable",values="value",
                       title="Usage of transportation modes per Month",
                       labels={"value": "Passengers", "Period and Financial year": "Year / Month",
                               "variable": "Mode of Transportation"}
                       )
    pie_chart.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    #pie_chart.show()
    figurestoshow.append(pie_chart)
    return figurestoshow

