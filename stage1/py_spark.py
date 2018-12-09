from numpy import array
from math import sqrt
import pandas as pd
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel



sc = SparkContext()
# df = pd.read_csv('/media/sumanthvrao/Personal/PESU/SEMESTER 5/BigData/Project/batsman.csv')
# df = df[['Innings_batted','Runs','Batting_strike_rate']]
# # Load and parse the data
##df.to_csv('/home/sumanthvrao/bigdata/out.csv')

data = sc.textFile("project/out.csv")

parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))

# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 10, maxIterations=10, initializationMode="random")

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))


def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)

# centers = clusters.centers()
# print("Cluster Centers: ")
# for center in centers:
#     print(center)

# Save and load model
clusters.save(sc, "file:///home/sumanthvrao/bigdata/")
sameModel = KMeansModel.load(sc, "file:///home/sumanthvrao/bigdata/")

from pyspark.sql import SQLContext
sqlContext = sqlContext(sc)

df = sqlContext.read.parquet("file:///home/sumanthvrao/bigdata/data/")