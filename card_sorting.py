from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

papers = [
    {"title": "Estimating and adapting to registration errors in augmented reality systems",
     "keywords": ["registration error", "error detection"]},
    {"title": "PredART: Towards Automatic Oracle Prediction of Object Placements in Augmented Reality Testing",
     "keywords": ["test oracle", "object placement", "error detection"]},
    {"title": "Virtual Reality Collision Detection Based on Improved Ant Colony Algorithm",
     "keywords": ["collision detection"]},
    {"title": "Test-retest reliability of the virtual reality sickness evaluation using electroencephalography (EEG)",
     "keywords": ["cybersickness", "EEG"]},
    {"title": "An automated functional testing approach for virtual reality applications",
     "keywords": ["test data generation", "test requirements"]},
]

cards = [f"{paper['title']}: {', '.join(paper['keywords'])}" for paper in papers]

documents = [" ".join(paper['keywords']) for paper in papers]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

num_clusters = 3

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

for i, label in enumerate(kmeans.labels_):
    print(f"Paper: {papers[i]['title']} -> Cluster {label}")

df = pd.DataFrame({'Paper Title': [paper['title'] for paper in papers], 'Cluster': kmeans.labels_})
print(df)