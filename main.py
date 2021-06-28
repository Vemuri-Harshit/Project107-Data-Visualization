import pandas as pd;
import csv;
import plotly.graph_objects as px;

df = pd.read_csv('marks.csv');
print('hi');

data = px.Figure(px.Bar(x= df.groupby('student_id')['attempt'].mean(), y= ['level 1', 'level 2', 'level 3', 'level 4'],orientation = 'h'));
data.show();