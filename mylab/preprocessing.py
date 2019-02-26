from shared_keys.shared_keys import *
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class DataPreprocessing():
    @staticmethod
    def scale_down_data(numeric_data, scaling_range=(0,10)):
        # provide the scaling range
        numeric_data = numeric_data.fillna(0)
        scaler = MinMaxScaler(feature_range=scaling_range)
        return pd.DataFrame(scaler.fit_transform(numeric_data), columns=numeric_data.columns)

class DataFrameUtilOperations():
    @staticmethod
    def get_columns_as_numeric_and_nominal(input_data_frame, columns_to_exclude):
        numeric_cols = [x for x in input_data_frame._get_numeric_data().columns if x not in columns_to_exclude]
        nominal_cols = [x for x in input_data_frame.columns if x not in numeric_cols]
        nominal_cols = [x for x in nominal_cols if x not in columns_to_exclude]
        return {'NumericalColumns':numeric_cols, 'CategoricalColumns':nominal_cols}
    # def impute_missing_values():

    # def discretize_data(numeric_data):
