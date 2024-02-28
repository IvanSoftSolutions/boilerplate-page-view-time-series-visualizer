import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean() 
    df_bar=df_bar.unstack()

    # Draw bar plot    
    fig= df_bar.plot.bar(legend=True, figsize= (10,5), ylabel='Average Page Views',       
    xlabel='Years').figure
    plt.legend(['January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(10,5), dpi= 80)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(xlabel = "Year", ylabel = "Page Views", title = "Year-wise Box Plot (Trend)")
    sns.boxplot(x='month', y='value', data=df_box, order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], ax=axes[1]).set(xlabel = "Month", ylabel = "Page Views", title = "Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

#############################################################################################################################################################################################################################################

    # Copy and modify data for monthly bar plot
    # df_bar = df.copy()
    # df_bar.reset_index(inplace=True)
    # df_bar['year'] = pd.to_datetime(df_bar['date']).dt.year
    # df_bar['month'] = pd.to_datetime(df_bar['date']).dt.month_name()
    # df_bar = df_bar.drop(columns=['date'])
    
    # years_list = df_bar['year'].unique()
    # months_list = df_bar['month'].unique()    
    
    # year_month_dict = {}
    # for year in years_list:
    #     year_month_dict[year] = dict.fromkeys(list(df_bar[df_bar['year'] == year]['month'].unique()))
    
    # for year in year_month_dict:
    #     for month in year_month_dict[year]:
    #         year_month_dict[year][month] = df_bar[(df_bar['year'] == year) & (df_bar['month'] == month)]['value'].mean()
    
    # df_bar =  pd.DataFrame.from_dict(data=year_month_dict, orient='index', columns= ['January', 'February', 'March' ,'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    # df_bar = df_bar.sort_index()
    
    # Draw bar plot
    # fig = df_bar.plot.bar(xlabel='Years', ylabel='Average Page Views').figure