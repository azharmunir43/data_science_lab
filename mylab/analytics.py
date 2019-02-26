import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as stats
import numpy as np
import seaborn as sns
import pandas as pd

font = {'family': 'sans-serif', 'weight': 'normal', 'size': 12}
matplotlib.rc('font', **font)
# matplotlib.rcParams['figure.figsize'] = (12.0, 5.0)
#
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
matplotlib.rc('axes', labelsize=13)
matplotlib.rc('axes', titlesize=15)

from mylab.preprocessing import *


class TargetAnalytics():
    ReportedVariables = []

    @staticmethod
    def custom_barplot(df, output_filename='', col1='', Export=False):
        f, (ax0, ax1) = plt.subplots(1, 2)
        df[col1].value_counts().plot(ax=ax0, kind='bar')
        ax0.set_title('Bar Plot of {}'.format(col1))
        df[col1].value_counts().plot(ax=ax1, kind='pie')
        ax1.set_title('Pie Chart of {}'.format(col1))
        if Export:
            f.savefig(output_filename)
            plt.close()
        else:
            plt.show()


class NumericAnalytics():
    @staticmethod
    def shapiro_test(x):
        p_val = round(stats.shapiro(x)[1], 6)
        status = 'passed'
        color = 'blue'
        if p_val < 0.05:
            status = 'failed'
            color = 'red'
        return status, color, p_val

    @staticmethod
    def custom_barplot(df, output_filename='', col1='', Export=False):
        fig, axes = plt.subplots(2, 2)
        axes = axes.reshape(-1)
        #     print df[col].describe()
        df[col1].plot(ax=axes[0], kind='hist')
        axes[0].set_title('Histogram of {}'.format(col1))
        df[col1].plot(ax=axes[1], kind='kde')
        axes[1].set_title('Density Plot of {}'.format(col1))
        ax3 = plt.subplot(223)
        stats.probplot(df[col1], plot=plt)
        axes[2].set_title('QQ Plot of {}'.format(col1))
        df[col1].plot(ax=axes[3], kind='box')
        axes[3].set_title('Box Plot of {}'.format(col1))
        status, color, p_val = NumericAnalytics.shapiro_test(df[col1])
        fig.suptitle('Normality test for {} {} (p_value = {})'.format(col1, status, round(p_val, 6)), color=color,
                     fontsize=12)
        if Export:
            fig = plt.gcf()
            plt.tight_layout()
            fig.set_size_inches(16, 12)
            fig.savefig(output_filename)
            plt.close()
        else:
            plt.show()


class CategoricAnalytics():
    @staticmethod
    def custom_barplot(df, output_filename='', col1='', Export=False):
        fig, (ax0, ax1) = plt.subplots(1, 2)
        df[col1].value_counts().nlargest(10).plot(ax=ax0, kind='bar')
        ax0.set_xlabel(col1)
        ax0.set_title('Bar chart of {}'.format(col1))
        df[col1].value_counts().nlargest(10).plot(ax=ax1, kind='pie')
        ax1.set_title('Pie chart of {}'.format(col1))
        if Export:
            fig = plt.gcf()
            # plt.tight_layout()
            fig.set_size_inches(16, 12)
            fig.savefig(output_filename)
            plt.close()
        else:
            plt.show()


class DataAnalytics():
    @staticmethod
    def plot_basic_stats_of_data(df, output_filename='', data_title='', Export=False):

        fig, ax = plt.subplots(1)
        null = pd.DataFrame(df.isnull().sum(), columns=['Null'])
        count = pd.DataFrame(df.count(), columns=['Values Found'])
        unique = pd.DataFrame(df.nunique(), columns=['Unique'])
        basic_stats = null.join(unique).join(count)
        basic_stats['Column Name'] = basic_stats.index
        # basic_stats = basic_stats.reset_index(drop=True)
        basic_stats.plot.bar(ax=ax)
        if data_title != '':
            ax.set_title('Basic Stats of ' + data_title)
        else:
            ax.set_title('Basic Stats of Data')

        if Export:
            fig = plt.gcf()
            plt.tight_layout()
            ax.legend(loc='upper right')
            fig.set_size_inches(16, 12)
            fig.savefig(output_filename)
            plt.close()
            # return fig
        else:
            plt.show()


    @staticmethod
    def frequency_plot(input_data_frame,
                       bins_to_be_cut=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                       column_to_plot = '',
                       target_columns_name='',
                       data_title='',
                       hue_order=[],
                       output_filename='',
                       Export=False):

        fig, ax = plt.subplots(1)
        if data_title != '':
            ax.set_title('Target Class Wise Distribution of ' + data_title + ' For Column - ' + column_to_plot)
        else:
            ax.set_title('Target Class Wise Distribution of Data')

        input_data_frame['scoresBinned'] = pd.cut(input_data_frame[column_to_plot], bins_to_be_cut)
        sns.countplot(data=input_data_frame, x='scoresBinned', hue=target_columns_name, hue_order=hue_order)
        ax.set_xlabel(column_to_plot, fontsize=11)
        ax.set_ylabel('Class Wise Frequency', fontsize=11)
        fig = plt.gcf()
        # plt.tight_layout()
        ax.legend(loc='upper right')
        fig.set_size_inches(16, 12)
        # modified = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        # ax.set_xticklabels(modified)
        # print(modified)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        if Export:

            fig.savefig(output_filename)
            plt.close()
            # return fig
        else:
            plt.show()
        del input_data_frame['scoresBinned']



    @staticmethod
    def plot_destribution_analysis_for_numeric(input_data_frame,
                                               kind='hist',
                                               consider_custom_numeric_classification=False,
                                               custom_defined_numeric_cols=[],
                                               cols_to_exclude=[],
                                               data_title='',
                                               output_filename='',
                                               Export=False):

        if consider_custom_numeric_classification:
            numeric_cols = custom_defined_numeric_cols
        else:
            col_dict = DataFrameUtilOperations.get_columns_as_numeric_and_nominal(input_data_frame,
                                                                                  columns_to_exclude=cols_to_exclude)
            numeric_cols = col_dict['NumericalColumns']

        fig, ax = plt.subplots(1)

        if kind == 'hist':
            pd.DataFrame.hist(data=input_data_frame,
                              column=numeric_cols,
                              ax=ax,
                              grid=False,
                              sharex=True, sharey=True)
        if kind == 'box':
            pd.DataFrame.boxplot(data=input_data_frame,
                                 column=numeric_cols,
                                 grid=False,
                                 sharex=True, sharey=True, ax=ax)
        if data_title != '':
            ax.set_title('Basic Stats of ' + data_title)
        else:
            ax.set_title('Basic Stats of Data')
        fig = plt.gcf()
        plt.tight_layout()
        fig.set_size_inches(16, 12)
        if Export:

            fig.savefig(output_filename)
            plt.close()
            # return fig
        else:
            plt.show()

    @staticmethod
    def column_distribution_analysis(input_data_frame,
                                     column_to_plot='',
                                     target_column='',
                                     data_title='',
                                     output_filename='',
                                     Export=False):

        grouped = input_data_frame.groupby(target_column)
        column_summary_data_frame = grouped[column_to_plot].agg([np.max, np.mean, np.min, np.std])
        column_summary_data_frame.columns = ['Max', 'Mean', 'Min', 'Std']
        fig, ax = plt.subplots(1)

        column_summary_data_frame.plot(kind='bar', ax=ax)

        if data_title != '':
            ax.set_title('Basic Stats of {} in {}'.format(column_to_plot, data_title))
        else:
            ax.set_title('Basic Stats of column {}'.format(column_to_plot))
        ax.grid(False)
        fig = plt.gcf()
        plt.tight_layout()
        ax.legend(loc='upper right')
        fig.set_size_inches(16, 12)

        if Export:
            fig.savefig(output_filename)
            plt.close()
        else:
            plt.show()

    @staticmethod
    def correlation_analysis(input_data_frame,
                            consider_custom_defined_numericals = False,
                            custom_numeric_cols_to_plot = [],
                            cols_to_exclude = [],
                            output_filename = '',
                            Export = False
                            ):
        if consider_custom_defined_numericals:
            numeric_cols = custom_numeric_cols_to_plot
        else:
            col_dict = DataFrameUtilOperations.get_columns_as_numeric_and_nominal(input_data_frame,
                                                                                  columns_to_exclude=cols_to_exclude)
            numeric_cols = col_dict['NumericalColumns']


        # Create Dataframe containing only numerical features
        numeric_data_frame = input_data_frame[numeric_cols]
        fig, ax = plt.subplots(figsize=(16, 12))
        plt.title('Pearson Correlation of Features')

        sns.heatmap(numeric_data_frame.astype(float).corr(), linewidths=0.25, vmax=1.0, square=True, cmap="cubehelix",
                    linecolor='k', annot=True)
        ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
        ax.set_yticklabels(ax.yaxis.get_majorticklabels(), rotation=45)
        ax.grid(False)

        if Export:
            fig.savefig(output_filename)
            plt.close()
        else:
            plt.show()