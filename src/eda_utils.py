import matplotlib.pyplot as plt
import seaborn as sns


def plot_boxplot(df, column):

    plt.figure(figsize=(8,5))

    sns.boxplot(x=df[column])

    plt.title(f"Boxplot of {column}")

    plt.show()