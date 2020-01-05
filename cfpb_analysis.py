import pandas as pd
import zipfile, requests, io
from collections import Counter
from sklearn.utils import shuffle
from nltk.corpus import stopwords
import re

def top_100_companies(url_link, file, limit):

    r = requests.get(url_link)
    
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    
    frame = pd.read_csv(z.open(file))
    frame = shuffle(frame)
    frame = frame[:limit]
    frame = frame[pd.notnull(frame['Consumer complaint narrative'])]
    frame = frame.astype(str)
    
    stop_words = set(stopwords.words('english'))
    
    full_list = sorted(list(dict(frame['Company'].value_counts()[:100]).keys()))
    
    frame = frame[frame['Company'].isin(full_list)]
    
    v_groupby = {}

    frame['Year'] = [date[:7] for date in frame['Date received']]
    frame['Company'] = frame['Company'].str.upper()
    frame['Match Key'] = frame['Year'] + frame['Company']

            # group your chosen parameter by year in a dictionary
    groupby = dict(frame.groupby('Year')['Company'].apply(list))
    
    complaint_groupby = dict(frame.groupby('Match Key')['Consumer complaint narrative'].apply(list))
    
    complaint_groupby = {k: " ".join(v) for k, v in complaint_groupby.items()}
    
    for k, v in groupby.items():
        c = Counter(v)
        v_groupby[k] = c.most_common()

            # plot the figure
    frame = pd.DataFrame([(k, *t) for k, v in v_groupby.items() for t in v], columns=['month','company','complaints'])
    
    frame['Match Key'] = frame['month'] + frame['company']
    
    frame['complaints_description'] = frame['Match Key'].map(complaint_groupby)
    
    frame['complaints_description'] = frame['complaints_description'].str.lower()
    
    frame = frame.drop('Match Key', axis = 1)
    
    frame['complaints_description'] = frame['complaints_description'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
    
    frame['complaints_description'] = [re.sub(r'x{2,}','', x) for x in frame['complaints_description']]

    return frame
