import numpy as np
from plotly import graph_objects as go

if __name__ == '__main__':
    # Define the function
    x = np.linspace(-5, 5, 1000)  # Generate x values from -5 to 5
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    y = a * x ** 2 + b * x + c

    # Create the plot using Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'y={a}x^2+{b}x+{c}'))

    # Customize the layout
    fig.update_layout(
        title=f'Plot of y = {a}x^2+{b}x+{c}',
        xaxis_title='x',
        yaxis_title='y',
        showlegend=True,
        template='plotly_white'
    )

    # Show the plot
    fig.show()
