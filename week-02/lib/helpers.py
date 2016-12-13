import seaborn as sns

def stripplot_by_year(dataframe):
    """
    Takes a transposed water data dataframe as argument.
    Plots a stripplot for each year.
    """
    
    for i in range(119):
        plot = sns.stripplot(y=dataframe[i], x=dataframe['Year'])
    return plot