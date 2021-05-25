import os
import pandas as pd
import numpy as np

def get_colnames(dataset_path):
	colnames = pd.read_csv(os.path.join(dataset_path,'features.txt'),
		delim_whitespace=True, header=None, index_col=0)
	
	duplicated_cols = colnames.loc[colnames.duplicated()].index		
	unique_duplicated_colnames = np.unique(colnames.loc[colnames.duplicated()])
	y_z_cols_duplicated = colnames.loc[colnames.duplicated()]
	y_cols_duplicated = y_z_cols_duplicated.loc[~ y_z_cols_duplicated.duplicated()]
	z_cols_duplicated = y_z_cols_duplicated.loc[y_z_cols_duplicated.duplicated()]

	y_cols_duplicated = y_cols_duplicated.apply(lambda name: name + '_Y') 
	z_cols_duplicated = z_cols_duplicated.apply(lambda name: name + '_Z')

	x_set = set(unique_duplicated_colnames)
	y_z_cols_renamed = pd.concat([y_cols_duplicated, z_cols_duplicated])
	colnames.loc[duplicated_cols] = y_z_cols_renamed
	new_colnames = colnames.apply(lambda row: row[1] + '_X' if row[1] in x_set else row[1], axis=1)
	
	return new_colnames


def get_x(dataset_path):
	X = pd.read_csv(os.path.join(dataset_path,'train','X_train.txt'), 
		header=None, delim_whitespace=True, error_bad_lines=False)
	return X


def get_activity(dataset_path):
	activity = pd.read_csv(os.path.join(dataset_path, 'train', 'y_train.txt'),
		header=None, names=['activity'])
	activity['activity'] = activity['activity'].map({
		1: 'WALKING',
		2: 'WALKING_UPSTAIRS',
		3: 'WALKING_DOWNSTAIRS',
		4: 'SITTING',
		5: 'STANDING',
		6: 'LAYING'})
	return activity
		
def get_subject(dataset_path):
	subjects = pd.read_csv(os.path.join(dataset_path, 'train', 'subject_train.txt'),
		header=None, names=['subject'])
	return subjects
		
def get_data_train(dataset_path='UCI HAR Dataset'):
	columns = get_colnames(dataset_path)
	X = get_x(dataset_path)
	X.columns = columns
	activity = get_activity(dataset_path)
	subject = get_subject(dataset_path)
	df = pd.concat([X, activity, subject], axis=1)
	return df
