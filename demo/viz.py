import pandas as pd
import matplotlib.pyplot as plt


def pool(x):
    oldi = -1
    group_num = 1
    for i in range(10, 101, 10):
        if (x > oldi and x <= i):
            return group_num
        group_num += 1
    return group_num

def visualize(filepath):
    df = pd.read_csv(filepath)

    # get count of people in each video
    df = df.groupby(["name"]).count()

    # get number of videos with each unique count
    df = df.drop(columns="prop")
    df = df.reset_index()
    df = df.groupby(["id"]).count()

    # pooling
    df = df.groupby(by=pool).sum()
    print(df)
    df = df.reset_index() # so we can access "id"
    # plt.bar(df.loc[:, "id"], df.loc[:, "name"], 1)
    plt.bar(df.loc[:, "id"].astype("string"), df.loc[:, "name"], 0.5)
    plt.savefig('../results/barchart.png')

if __name__ == "__main__":
    filepath = "../results/stats.csv"
    visualize(filepath)
