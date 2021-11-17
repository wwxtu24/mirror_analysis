df.nunique()
df['c1']=df['c1'].unique()
df.info()
df.describe()
df.value_counts()
df.isnull().sum()
df.group('v_type')['cnt'].mean().values()
df.group('v_type').agg({'cnt':np.mean(),'amt':np.sum()})

pivot：透视图
	df.group('v_type').agg({'cnt':np.mean()).fillna(0)
	tmp_pivot = pd.pivot_table(data=df,index='v_type',values='cnt',aggfunc='mean',fill_value=0)
pd.get_dummys()

sklearn.preprocessing.LabelBinarizer
sklearn.preprocessing.OneHotEncoder
sklear.feature_extract.DictVectorizer

dask/hdf5