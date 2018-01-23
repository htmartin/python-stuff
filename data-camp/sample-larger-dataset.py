#!/usr/bin/env python

import pandas as pd 
import numpy as np

col_names=['id', 'topic', 'units_viewed', 'days_ago']

user_topic=pd.read_csv('~/taylor-oreilly/tmp/user_cube.tsv', sep='\t', header=None, names=col_names)


user_topic_sample=user_topic.sample(frac=0.1)

print(user_topic_sample.info())

#user_topic_sample= user_topic_sample.sort_values('impact')

#hist=user_topic_sample.salesforce_id.value_counts()

print(user_topic_sample.head())

#salesforce_id     object
#term              object
#impact           float64
#delta              int64