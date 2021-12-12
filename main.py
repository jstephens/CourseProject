from flask import Flask, render_template,request
import plotly
import json
import plotly.express as px
import pandas as pd

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
    feature =  'In Our Time'
    print(feature)
    bar = create_plot(feature)
    return render_template('index.html', plot=bar)

def create_plot(feature):      
    featurefile = feature.replace(' ','_')
    datafile = './Inputs/novels/'+featurefile+'_df.csv'
    datasource = pd.read_csv(datafile)
    
    title = 'Emotional Path Through '+feature
    data = px.line(datasource, x="chapterno", y="score", title=title, hover_data=["words"])
  #  data = px.imshow(datasou)
    data.update_layout(width=450, height=450,margin_l=1)
    
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON= create_plot(feature)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)
