import numpy as np
from plotly import graph_objects as go

if __name__ == '__main__':
    # Define the function
    x = np.linspace(-5, 5, 1000)  # Generate x values from -5 to 5
    y = x ** 2 - 1 * x - 2

    # Create the plot using Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'y=ax^2+bx+c'))

    # Customize the layout
    fig.update_layout(
        title='Plot of y = ax^2+bx+c',
        xaxis_title='x',
        yaxis_title='y',
        showlegend=True,
        template='plotly_white'
    )

    # Show the plot
    fig.show()
