# https://github.com/pandas-profiling/pandas-profiling
# !pip install pandas_profiling # use this if you have not already installed pandas_profiling package (!) is to run command line arguments in jupyter notebook
import pandas_profiling
report = pandas_profiling.ProfileReport(df)
report.to_notebook_iframe() # for jupyter notebook, otherwise just use report
