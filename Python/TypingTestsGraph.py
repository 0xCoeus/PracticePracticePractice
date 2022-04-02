import plotly.graph_objects as go   

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

avg_score = [70.5, 85, 90, 87.5, 70, 71.7, 69.2, 76.8, 65, 69.5, 81.8, 75.9, 69, 70.8, 79.8, 76.1, 77, 76.4, 83.5, 80, 83.5, 81, 80.2, 77.1, 79.3, 85.3, 86.5, 86.8, 89.5]
highest_score = [80, 97, 97, 96, 79, 82, 80, 85, 73, 80, 96, 91, 77, 80, 89, 87, 85, 88, 89, 88, 96, 90, 92, 84, 86, 91, 94, 96, 95]

fig = go.Figure()

fig.add_trace(go.Scatter(x=days, y=avg_score, name='Average Score', line=dict(color='royalblue', width=3)))
fig.add_trace(go.Scatter(x=days, y=highest_score, name='Highest Score', line=dict(color='firebrick', width=3)))

fig.update_layout(title='Typing Challenges Data', xaxis_title = 'Days', yaxis_title = 'Words Per Minute (WPM)')

fig.show()