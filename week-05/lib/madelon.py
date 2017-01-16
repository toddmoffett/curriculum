import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

feature_datafile_location = "/Users/toddmoffett1/DSI/dsi_repo/DSI_SM_3/data/madelon_data.csv"
target_datafile_location = "/Users/toddmoffett1/DSI/dsi_repo/DSI_SM_3/data/madelon_labels.csv"

def load_madelon_set_into_df():
    '''
    load madelon data
    return madelon_feature_df, madelon_target_df
    '''
    madelon_feature_df = pd.read_csv(feature_datafile_location,
                                     sep=' ',
                                     header=None)
    madelon_feature_df.columns = ['feat_' + str(col) 
                                  for col in madelon_feature_df.columns]


    madelon_target_df = pd.read_csv(target_datafile_location,
                                    header=None)
    madelon_target_df.columns = ['trgt_' + str(col) 
                                 for col in madelon_target_df.columns]
    
    return madelon_feature_df, np.ravel(madelon_target_df)

def standard_classification(model, X, y, model_args,random_state_split,):
    X_train,     \
        X_test,  \
        y_train, \
        y_test = train_test_split(X, y, 
                                  random_state=random_state_split)

    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)
    
    this_model = model(**model_args)
    this_model.fit(X_train, y_train)
    
    training_predictions = this_model.predict(X_train)
    testing_predictions = this_model.predict(X_test)
    
    this_model_class_name = this_model.__class__.__name__
    this_model_args = ' '.join([str(key)+':'+str(val) 
                     for key,val in model_args.items()])
    
    print("{} {}".format(this_model_class_name,
                         this_model_args))
    
    return {'model': this_model,
            'y_train_pred' : training_predictions,
            'y_test_pred' : testing_predictions,
            'X_test' : X_test,
            'X_train' : X_train,
            'y_test' : y_test,
            'y_train' : y_train}