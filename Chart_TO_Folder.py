import dataiku
import pandas as pd
import matplotlib.pyplot as plt
import os
import io

# Read recipe inputs
un_data_prepared = dataiku.Dataset("un_world_cities_prepared")
df = un_data_prepared.get_dataframe()

# top 10 most populous countries
TOP_10 = ['India', 'China', 'Brazil', 'Japan', 'Pakistan', 'Mexico', 'Nigeria',
                'United States of America', 'Indonesia', 'Turkey']

# generate plot for each country and save to folder
for country in TOP_10:

        df_filtered = df[df['Country or area'] == country]

        y = range(0, len(df_filtered))
        x_1 = df_filtered["avg_roc_2000-2016"]
        x_2 = df_filtered["avg_roc_2016-2030"]

        fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(12, 9))

        fig.patch.set_facecolor('xkcd:light grey')
        plt.figtext(.5,.9, "Pop. ROC Comparison ", fontsize=15, ha='center')

        axes[0].barh(y, x_1, align='center', color='royalblue')
        axes[0].set(title='2000-2016')
        axes[1].barh(y, x_2, align='center', color='red')
        axes[1].set(title='2016-2030')

        axes[1].grid()
        axes[0].set(yticks=y, yticklabels=df_filtered['City'])
        axes[0].invert_xaxis()
        axes[0].grid()

        # Write recipe outputs
        pyramid_plot = dataiku.Folder("population_growth_comparisons")

        bs = io.BytesIO()
        plt.savefig(bs, format="png")
        pyramid_plot.upload_stream(country + "_fig.png", bs.getvalue())
