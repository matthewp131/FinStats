import plotly
import plotly.graph_objs as grapher
import utils

def line(dictionary, x_key, y_key, symbol):
    trace = grapher.Scatter(
        x = dictionary[x_key],
        y = dictionary[y_key]
    )

    data = [trace]
    layout = {
        "title": y_key + " for " + symbol,
        "xaxis": {"title": x_key},
        "yaxis": {"title": y_key + " (" + utils.units[y_key] + ")"}
    }

    plotly.offline.plot({"data": data,
                         "layout": layout})