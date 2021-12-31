import pandas as pd
import argparse

def analyse(path, file_name):
    dataframe = pd.read_csv(path+"/"+file_name)
    df = dataframe.describe(include='all')
    # 1- best/worst 3 posts
    max = dataframe.sort_values(by="reactions_count", ascending=False).head(3)
    colonnes = ["id", "shares", "reactions_count", "comments", "content"]
    max = pd.DataFrame(max[colonnes])
    max.to_csv(path+"/max.csv")
    min = dataframe.sort_values(by="reactions_count").head(3)
    min = pd.DataFrame(min[colonnes])
    min.to_csv(path+"/min.csv")
    # 2-Distribution of reacts
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    plot1 = sns.displot(dataframe, x="reactions_count", kde=True)
    plot1.set(title='Distribution of reacts')
    plot1.savefig(path+'/plot1.jpeg')
    plot2 = sns.relplot(x="reactions_count", y="comments", kind="line", data=dataframe);
    plot2.set(title='reacts distribution % comments')
    plt.show()
    plot2.savefig(path+'/plot2.jpeg')
    # 3- mean,max,min of reacts and comments
    table1 = dataframe.agg({'likes': ['mean', 'min', 'max'], 'loves': ['mean', 'min', 'max'], 'haha': ['mean', 'min', 'max'],
                     'wow': ['mean', 'min', 'max'], 'cares': ['mean', 'min', 'max'], 'sad': ['mean', 'min', 'max'],
                     'angry': ['mean', 'min', 'max'], 'haha': ['mean', 'min', 'max'],
                     'comments': ['mean', 'min', 'max']})
    table1
    table1.to_csv(path+"/table1.csv")
    # 4-with most missing data
    d1 = dataframe.isna().sum()
    d1 = pd.DataFrame([d1])
    i = d1.idxmax(axis=1)
    d1 = pd.DataFrame(d1[i])
    d1.to_csv(path+"/missingdata.csv")
    # 5-average length of content
    column = ["content"]
    dataframe[column]
    da = dataframe["content"].dropna()
    l = []
    for i in da:
        p = len(i)
        l.append(p)
    data = {"len_content": l}
    d = pd.DataFrame(data)
    d_mean = d.mean()
    print('analyse is DONE')

parser = argparse.ArgumentParser(description='analyse facebook page by giving the name and the postes number')
parser.add_argument('path', type=str, help='path')
parser.add_argument('file_name', type=str, help='page name')
args = parser.parse_args()

if __name__=='__main__':
    print(analyse(args.path, args.file_name))

