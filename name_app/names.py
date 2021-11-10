from django import forms
from django.shortcuts import render

import pandas as pd
import altair as alt

class NameRequestForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    state = forms.CharField(label="State", required=False, min_length=2, max_length=2)

def name_form(request):
    """
    Takes in a request. If the method was POST, it will assume 
        it was the user giving sending name request data

    Renders various pages based on the data given
    """
    if request.method == "POST":
        # Receives the request message and saves it to a form
        form = NameRequestForm(request.POST)

        if form.is_valid():
            # Grabs the name and state info from the data
            name = form.cleaned_data["name"].capitalize()
            state = form.cleaned_data["state"].upper()

            # Links to the no_valid_name html page if an invalid name was typed in
            if name.strip() == "":
                return render(request, 'name_app/no_valid_name.html', {})

            # Grabs the graph urls from the name processing function
            urls = process_name(name, state)

            # If there aren't any urls, it will go back to the invalid page
            if not urls:
                return render(request, 'name_app/no_valid_name.html', {})

            # Renders the name data page with the images linked
            return render(request, "name_app/name_data.html", {
                "name": name,
                "total_url": urls[0],
                "state_url": urls[1] if len(urls) > 1 else ""})

    # In the event that it is the first time loading the page, and it wasn't a submission, it will create an empty form
    else:
        form = NameRequestForm()

    # Renders the request page with the form
    return render(request, 'name_app/name_request.html', {'form': form})

def process_name(name:str, state:str):
    """
    Takes a name and a state. If the state is empty, it will only do a return a url for the totals.
    Returns a list of urls that link to graphs that were created.
    If there are no results for the name, it will instead return False.
    """
    # Creates an empty list for the urls
    urls = []

    # Sets the data url
    url = "name_app/static/data/names_year.csv"

    # Reads in the data as a pandas object
    name_data = pd.read_csv(url)

    # Queries the data to get only the chosen name
    total_name_data = name_data.query(f'name == "{name}"')
    # If the query is empty, returns False
    if total_name_data.empty:
        return False

    # Resets the index so numbers display correctly in the rows
    total_name_data = total_name_data.reset_index()

    # Gets the max total, if it is 0, it returns False
    max_total = int(total_name_data.Total.max())
    if max_total == 0:
        return False

    # Gets the max total year
    max_total_year = total_name_data.query("Total == @total_name_data.Total.max()").year.values[0]
    
    # Sets a column for the max total year for use with annotations
    total_name_data["max_total_year"] = max_total_year

    # Charts the data, removing commas in the years axis and making year capital on the axis title
    total_name_data_chart_1 = (alt.Chart(total_name_data)
        .encode(
            x = alt.X(
                "year",
                axis=alt.Axis(format="d", title="Year")
            ),
            y = "Total")
        .properties(
            title=f"Babies With Name {name}"
        )
        .mark_line())

    # Creates a vertical line for the chart at the max total year
    total_name_data_chart_2 = alt.Chart(total_name_data).mark_rule().encode(
        x="max_total_year"
    )

    # Creates the annotation data to graph the annotation
    annotation_data = pd.DataFrame({"year":[max_total_year], "Total":[max_total/2], "text":[f" <- The name {name} was most popular in {max_total_year}\n    with {max_total} babies named"]})

    # Graphs the annotation
    annotation = alt.Chart(annotation_data).mark_text(
        align='left',
        baseline='middle',
        fontSize = 12,
        dx = 0
    ).encode(
        x="year",
        y="Total",
        text="text"
    )

    # Creates the save url and saves the image
    url = "name_app/static/data/name_chart.png"
    (total_name_data_chart_1 + total_name_data_chart_2 + annotation).save(url)

    # Adds the url to the list
    urls.append("data/name_chart.png")
    
    # If there isn't a given state or the state is invalid, it just returns the current urls
    if state == "" or state not in total_name_data.columns:
        return urls
    else:
        # Gets the max total, if it is 0, it returns the current urls list
        max_total = int(total_name_data[state].max())
        if max_total == 0:
            return urls

        # Gets the max total year
        max_total_year = total_name_data.query(f"{state} == @total_name_data['{state}'].max()").year.values[0]
        total_name_data["max_total_year"] = max_total_year

        # Charts the data, removing commas in the years axis and making year capital on the axis title
        total_name_data_chart_1 = (alt.Chart(total_name_data)
            .encode(
                x = alt.X(
                    "year",
                    axis=alt.Axis(format="d", title="Year")
                ),
                y = f"{state}:Q")
            .properties(
                title=f"Babies With Name {name} in {state}"
            )
            .mark_line())

        # Creates a vertical line for the chart at the max total year
        total_name_data_chart_2 = alt.Chart(total_name_data).mark_rule().encode(
            x="max_total_year"
        )

        # Creates the annotation data to graph the annotation
        annotation_data = pd.DataFrame({"year":[max_total_year], f"{state}":[max_total/2], "text":[f" <- The name {name} was most popular in {max_total_year}\n    with {max_total} babies named"]})

        # Graphs the annotation
        annotation = alt.Chart(annotation_data).mark_text(
            align='left',
            baseline='middle',
            fontSize = 12,
            dx = 0
        ).encode(
            x="year",
            y=f"{state}:Q",
            text="text"
        )

        # Saves the url for the graph
        url = "name_app/static/data/state_name_chart.png"
        (total_name_data_chart_1 + total_name_data_chart_2 + annotation).save(url)

        # Adds the url and returns them
        urls.append("data/state_name_chart.png")
        return urls