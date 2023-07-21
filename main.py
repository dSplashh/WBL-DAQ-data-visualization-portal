from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import glob

app = Flask(__name__)

tsv_directory = '/Users/darryl/Documents/sprint-june23/drive-download-20230626T183246Z-001/'
tsv_files = glob.glob(tsv_directory + '*.tsv')
myFiles = np.array(tsv_files)

#index = 12, 9, 0 ~ bad files

def getData(file):
    data = pd.read_table(file)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    data = getData(myFiles[1])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"
    
    return render_template('plot1.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)

@app.route('/chart2')
def chart2():
    data = getData(myFiles[2])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot2.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)

@app.route('/chart3')
def chart3():
    data = getData(myFiles[3])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot3.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart4')
def chart4():
    data = getData(myFiles[4])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot4.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart5')
def chart5():
    data = getData(myFiles[5])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot5.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart6')
def chart6():
    data = getData(myFiles[6])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot6.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart7')
def chart7():
    data = getData(myFiles[7])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot7.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart8')
def chart8():
    data = getData(myFiles[8])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"
    
    return render_template('plot8.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart9')
def chart9():
    data = getData(myFiles[10])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot9.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart10')
def chart10():
    data = getData(myFiles[11])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot9.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart11')
def chart11():
    data = getData(myFiles[13])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot11.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart12')
def chart12():
    data = getData(myFiles[14])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot12.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)
    
@app.route('/chart13')
def chart13():
    data = getData(myFiles[15])
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 0], mode='lines', name='accx'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 1], mode='lines', name='accy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 2], mode='lines', name='accz'), row=3, col=1)
    
    fig2 = make_subplots(rows=3, cols=1, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 3], mode='lines', name='gyrx'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 4], mode='lines', name='gyry'), row=2, col=1)
    fig2.add_trace(go.Scatter(x=data.iloc[:, 6], y=data.iloc[:, 5], mode='lines', name='gyrz'), row=3, col=1)
    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header1="1"

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header2="2"

    return render_template('plot13.html', graphJSON1=graphJSON1, header1=header1, graphJSON2=graphJSON2, header2=header2)

if __name__ == '__main__':
    app.run()