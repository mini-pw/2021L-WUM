import os
import pandas as pd
import numpy as np

from itertools import combinations, permutations
from scipy.special import kl_div


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

def get_columns(df:pd.DataFrame, n_cols:int=20, method:str='chosen', n_bins:int=5):
	if method not in ('chosen', 'avg'):
		raise ValueError("method parameter should be one of ('chosen', 'avg')")

	activities = np.unique(df['activity'])
	activities_dict = {activity: None for activity in activities}

	for activity in activities_dict.keys():
		numerical_features = df[df['activity']==activity].drop(['activity', 'subject'], axis='columns')
		activities_dict[activity] = numerical_features.apply(
			lambda column: 
			np.histogram(column, bins=n_bins, density=True, range=(-1,1))[0])
	
	combi_colnames = list(map('-'.join, list(permutations(activities,2))))
	combi_df = pd.DataFrame(columns = combi_colnames)

	numerical_features = df.drop(['activity', 'subject'], axis='columns').columns
	for feature in numerical_features:
		combi_df = combi_df.append(pd.Series(np.repeat(feature, 30), name=feature, index=combi_colnames))

	def replace_inf_and_sum(feature1, feature2, x):
		kl = kl_div(
			activities_dict[feature1][x],
			activities_dict[feature2][x])
		return sum(map(lambda x: 100 if x>100 else x, kl))

	def count_inf(feature1, feature2, x):
		return sum(
			np.isinf(          # tu zliczamy infy
				kl_div(
					activities_dict[feature1][x],
					activities_dict[feature2][x])))

	def take_median(feature1, feature2, x):
		return np.median(          
				kl_div(
					activities_dict[feature1][x],
					activities_dict[feature2][x]))
	
	def apply_to_column(column):
		feature1, feature2 = column.name.split('-')
		return column.apply(lambda x: replace_inf_and_sum(feature1, feature2, x)) 
		# w tej lambdzie można wybrać inną funkcję

	result = combi_df.apply(apply_to_column)
	if method == 'chosen':
		return result.apply(lambda x: max(x), axis=1).sort_values(ascending=False).head(n_cols).index.to_list()
	if method == 'avg':
		return result.apply(lambda x: sum(x), axis=1).sort_values(ascending=False).head(n_cols).index.to_list()

