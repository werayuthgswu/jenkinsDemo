import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.cluster import DBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import normalized_mutual_info_score
from gensim.models.coherencemodel import CoherenceModel

from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from bertopic.vectorizers import ClassTfidfTransformer
from bertopic.representation import MaximalMarginalRelevance

print("hello world")
