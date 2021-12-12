from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go
import glob, os
import pandas as pd
import json
import plotly.express as px

app = Flask(__name__)

# os.chdir("./Inputs/Novels/")
# books = []
# for file in glob.glob("*.txt"):
#     if "_processed" not in file:
#         filename = file
#         filename1 = file.replace('_',' ')
#         filename1 = filename1.replace('.txt','')
#         books.append(filename1)

@app.route('/')
def index():
    feature =  'In Our TIme'
    print(feature)
    bar = create_plot(feature)
    return render_template('index.html', plot=bar)

def create_plot(feature):    
    if 'n' in str(feature):
        examplething = [[0,0,0],
                     [3, 5, 8],
                     [2, 1, 13]]
    else:
        examplething = [[14,1, 3],
                     [2, 1, 6],
                     [2,3, 1]]    
        
    data = px.imshow(examplething)
    data.update_layout(width=1500, height=500)
    
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON= create_plot(feature)
    return graphJSON

if __name__ == '__main__':
    app.run()
