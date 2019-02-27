import matplotlib.pyplot as plt
import pandas as pd
from mylab.reporting import *
from mylab.analytics import *
import os
from assets.constants import *

# df = pd.read_excel(os.path.join(DATA_DIRECTORY, 'Final-2012-Raw-V0.1.xlsx'))
df = pd.read_csv(os.path.join(DATA_DIRECTORY,'final.csv'), low_memory=False)
# print(df.columns)
# conf_cols_dict = DataFrameUtilOperations.get_columns_as_numeric_and_nominal(input_data_frame=df, columns_to_exclude=[])

# print(conf_cols_dict)
# del df['Roll No']
# DataReporting.generate_data_summary_report(df,
#                                            os.path.join(HARD_COPIES_FOR_TEST_DATA_DIRECTORY,
#                                                         'Test-1.docx'),
#                                            'LUMS Data',
#                                            'Student data for Grade Prediction',
#                                            'Grade',
#                                            True)

#
# DataReporting.generate_data_summary_report(df,
#                                            os.path.join(HARD_COPIES_FOR_TEST_DATA_DIRECTORY,
#                                                         'POC_Data Summary Report.docx'),
#                                            'LUMS POC Data',
#                                            'Student Semester Course data for Grade Prediction',
#                                            '',
#                                            True)

# DataReporting.generate_data_quality_report_for_individual_columns(
#     input_data_frame = df,
#     consider_custom_defined_classification_of_columns=False,
#     conf_cols_dict={},
#     columns_to_exclude=['Roll No'],
#     output_filelame=os.path.join(HARD_COPIES_FOR_TEST_DATA_DIRECTORY,'Test-3.1.1.docx'),
#     data_title = 'LUMS POC Data',Export =True
#                                            )
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# conf_col_dict = {'CategoricalColumns':['TERM', 'CRSE_ID', 'STUDENT_GRADE', 'CLASS_NBR', 'MARK_OUT_OF','COURSE_TITLE',
#                                        'CLASS_SECTION', 'LAM_TYPE',  'ACAD_GROUP', 'SUBJECT', 'ACAD_CAREER', 'SSR_COMPONENT',
#                                        'LAM_REQUIRED', 'ASSESSED', 'INCL_IN_MID_TERM', 'COPY_GRADES','GRADE_AVAILABLE'],
#                  'NumericalColumns':['ENRL_TOT', 'LAM_WEIGHT']}
#     # ,'ColumnsToExclude':['STUDENT_ID', 'TERM_DESCR', 'DESCRIPTION', 'EXCLUDE_FROM_GRADE']}
#
#
# DataReporting.generate_data_interaction_and_quality_report(
#     df,
#     False,
#     {},
#     'Grade',
#     ['Roll No'],
#     os.path.join(HARD_COPIES_FOR_TEST_DATA_DIRECTORY, 'Test-1.2.docx'),
#     'LUMS Old Data',
#     True
# )
# *************************************************************************************************************************

# DataReporting.generate_data_interaction_and_quality_report(df,
#                                                            False,
#                                                            {},
#                                                            'Grades',
#                                                            ['Roll No', 'Grade', 'Grades', 'Midterms Percentile','Quiz Assignment Percentile','Difference_From_Average_Quiz_Assignment'],
#                                                            os.path.join(HARD_COPIES_FOR_TEST_DATA_DIRECTORY,'Test-1.2.1.docx'),
#                                                            'LUMS POC Data',
#                                                            ['A', 'B', 'C', 'D', 'F'],
#                                                            True
#                                                            )
#
# InteractionAnalytics.correlation_analysis(df,
#                                           True,
#                                           ['Assignment 1 [10.0]', 'Assignment 2 [10.0]','Assignment 3 [10.0]', 'Assignment 4 [10.0]'],
#                                           ['Roll No'],
#                                           'Grade_SA',
#                                           os.path.join(PROJECT_CACHE, 'temp_correlation_pair_plot.png'),
#                                           False)


# print(type(grouped.get_group('A')))

# InteractionAnalytics.rank_associations(df, conf_cols_dict,'grade', 1, 1, False,
#                                  os.path.join(PROJECT_CACHE, 'temp_multiple_numeric_plot.png') )
# DataReporting.describe_data_frame_as_excel(df, 'x-16-15.xlsx', True)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# InteractionAnalytics.nc_relation(df, df[['Quiz 2 [10.0]']], df[['Quiz 3 [10.0]']], '', False)
# print(type(((df.shape[0] - df.count()) / df.shape[0])*100))


# TargetAnalytics.custom_barplot(df,output_filename='', col1='Grade_SA', Export=False)
# CategoricAnalytics.custom_barplot(df,output_filename='', col1='Grade_SA', Export=False)
# NumericAnalytics.custom_barplot(df,output_filename='', col1='Labs', Export=False)
# DataAnalytics.plot_basic_stats_of_data(df, False)
# plt.show()









# generate_data_summary_report(df, 'Version 1.docx', 'LUMS Data', 'Students data for grade prediction')
# print(type(df.loc[0]['Roll No']))

# nominal_data = df.select_dtypes(include=[np.object])

# nominal_data.plot(kind='pie', subplots=True)
# ------------------------------------------------------------------------------------------------------------------------------------
# fig = plt.figure()
# fig.suptitle('LUMS Student Data'+'Data Summary Plot')
#
# ax = fig.add_subplot(111)
# summary = pd.DataFrame(df.isnull().sum(), columns=['Null'])
# summary1 = pd.DataFrame(df.count(), columns=['Values Found'])
# summary2 = pd.DataFrame(df.nunique(), columns=['Unique'])
# x = summary1.join(summary).join(summary2)


# x['Column Name'] = x.index
# print(x.columns)
# ax = sns.barplot(y=["Column Name"],hue = ['Values Found', 'Null', 'Unique'], data=df)

# d = x.plot(kind='bar'
# , ax=ax
# )
# print(type(d))
# ax.grid(False)
# plt.legend(bbox_to_anchor=(1.00, 1), loc=2, borderaxespad=0.)

# ax.set_title('LUMS Student Data')
# plt.tight_layout()
# plt.show()
# ------------------------------------------------------------------------------------------------------------------------------------

# x = x.T

# x = x.reset_index(drop=True)
# summary['Column Name'] = summary.index
# sns.countplot(df.isnull().sum())
# print(x)
# sns.barplot(x = '', hue="Column Name", data=x);

# print(type(df.isnull().sum()))
# generate_data_summary_report(df, 'azzzzha.docx', 'Grade Prediction Data for 2012', 'Data of LUMS students for the year 2012')

# sns.heatmap(df.corr())
# plt.show()

# x = df.corr('pearson')
#
# print(x)


# sns.set()
# sns.despine()
# print(df.columns)


# sns.set(style="whitegrid", color_codes=True)
# sns.set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})
# sns.set_style("whitegrid", {'axes.grid' : False})

# fig = plt.figure(1)
# 'Roll No', 'Assignment 1 [10.0]', 'Assignment 2 [10.0]',
#        'Assignment 3 [10.0]', 'Assignment 4 [10.0]', 'Quiz 1 [10.0]',
#        'Quiz 2 [10.0]', 'Quiz 3 [10.0]', 'Quiz 4 [10.0]', 'Quiz 5 [10.0]',
#        'Quiz 6 [10.0]', 'Quiz 7 [10.0]', 'Quiz 8 [10.0]', 'Quiz 9 [10.0]',
#        'Quiz 10 [10.0]', 'Quiz 11 [10.0]', 'Grade', 'Grade_SA', 'Assignments',
#        'Quizzes', 'Labs', 'Midterms'
# g = sns.pairplot(df,
#                  hue="Grade_SA",
#                  # hue_order=['A','B','C'],
#                  # markers=['o', 's', 'D'],
#                  vars=[
#                      'Assignment 1 [10.0]', 'Assignment 2 [10.0]',
#                      # 'Assignment 3 [10.0]', 'Assignment 4 [10.0]',
#                      # 'Quiz 1 [10.0]','Quiz 2 [10.0]', 'Quiz 3 [10.0]',
#                      # 'Quiz 4 [10.0]', 'Quiz 5 [10.0]','Quiz 6 [10.0]',
#                      'Quiz 7 [10.0]', 'Quiz 8 [10.0]', 'Quiz 9 [10.0]',
#                      # 'Quiz 10 [10.0]', 'Quiz 11 [10.0]','Assignments','Quizzes', 'Labs', 'Midterms'
#                  ],
#                  plot_kws={
#                      "s":15
#                  },
#                  kind='scatter',
#                  diag_kind='plot'
#                  # size=2.5,
#                  # aspect=1.5,
#                  # palette=sns.hls_palette(8, l=.3, s=.8)
#                  )
# g = g.map_diag(plt.hist)
# g = g.map_offdiag(plt.scatter)
# g = g.add_legend()

# handles = g._legend_data.values()
# labels = g._legend_data.keys()
# g.fig.legend(handles=handles, labels=labels, loc='upper center', ncol=1)
# g.fig.legend(handles=handles, labels=labels, loc='lower center', ncol=3)
# g.fig.legend(handles=handles, labels=labels, loc='upper left', ncol=3)
# g.fig.subplots_adjust(top=0.92, bottom=0.08)

# sns_plot = sns.pairplot(df, hue='Grade')
# nominal_data = df[[x for x in df.columns if df[x].dtype == np.object]]
# for c in nominal_data.columns:
#     sums = nominal_data.groupby([c]).size()
#     plt.pie(x=sums, labels=sums.index)
# print(nominal_data['Grade'].count())
# print(type(nominal_data.groupby('Grade_SA').size()))
# plt.show()
