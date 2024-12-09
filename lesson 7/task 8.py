import numpy as np
import plotly.express as px


def get_population(fail):
    with open(fail, "r") as f:
        next(f)
        data = {}

        for line in f:
            sog = line.split(",")[8]
            data[sog[0]] = int(sog[1])

    return data

if __name__ == '__main__':
    data = get_population('../lesson 7/failslesson4/test_100k.csv')
    data = dict(sorted(data.items(), key=lambda c: c[1]))
    fig = px.line(x=data.keys(), y=data.values())
    fig.show()
