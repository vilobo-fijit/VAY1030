import numpy as np
import plotly.express as px


def get_population(fail):
    with open(fail, "r") as f:
        next(f)
        data = {}

        for line in f:
            country = line.split(",")
            data[country[0]] = int(country[1])

    return data

if __name__ == '__main__':
    data = get_population('population_by_age_group.csv')
    data = dict(sorted(data.items(), key=lambda c: c[1], reverse=True))
    fig = px.bar(x=data.keys(), y=data.values())
    fig.show()


