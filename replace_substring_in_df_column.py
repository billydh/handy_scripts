import pandas as pd

def replace_substring_in_df_column(df_col, map_dict):
    df_col.replace(map_dict, regex=True, inplace=True)


# example
# df = pd.DataFrame({'title': ['Citigroup says 30 bln capital helps exceed target',
#                              'Williams No Anglican consensus on Episcopal Church',
#                              'Microsoft Vista corporate sales go very well']})
#
# constituents = pd.DataFrame({'symbol': ['MMM', 'C', 'MCR', 'WLM'],
#                              'name': ['3M', 'Citigroup', 'Microsoft', 'Williams']})
#
# const_dict = dict(zip(constituents['name'], constituents['symbol']))
#
# replace_substring_in_df_column(df['title'], const_dict)
