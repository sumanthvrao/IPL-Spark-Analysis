Predict outcomes of IPL Cricket Matches for year 2018 using like Spark

Code Repository: [https://github.com/sumanthvrao/IPL-Spark-Analysis](https://github.com/sumanthvrao/IPL-Spark-Analysis)

## Summary

Developed a score-wicket prediction model using Apache Spark MLlib to simulate the outcomes of Indian Premium League cricket matches during 2018 season. Ball-by-ball data from previous matches was used to develop two simulation models - Bayesian probability-based and Decision tree-based. The Bayesian model used cumulative probabilities to predict different runs and wicket chances on each ball delivery. If the batsman-bowler data was missing/insufficient their cluster data (clustered using k-means clustering) was used.  The Decision tree model used cluster average data like average strike rate to train and predict the outcomes of 10 matches.

## Design

### PHASE 1 : CLUSTERING

Used k-means clustering on batsmen and bowlsers to group them into clusters based on numerous attributes. These clusters help estimate scores / wickets for a batsman-bowler pair who haven't squared off before and whose data isn't avaiable. Attributes used for batsman cluster are innings batted, runs scored, batting strike rate, while those for bowler cluster are innings bowled, wickets taken, Average and Economy.

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage1/Clustered.png?raw=true" alt="Batsman cluster visualization" width="500" height="400">

Using the plot of the number of clusters vs cost (within-cluster sum of square (WSS)). We found the elbow point for both the batsman and bowler cluster. The elbow point basically signifies that even after increasing the number of clusters the cost remains the same after this point. With the results of the batsman and bowler graphs we got these results:

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage1/elbow.png?raw=true" alt="Elbow curve" width="500" height="400">

Number of batsman cluster: 10

Number of bowler clusters: 11

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage1/player_predictions.png?raw=true" alt="Player predictions" width="500" height="400">

### PHASE 2 : PROBABILITY SIMULATION

The first step involved calculating probabilities of a batsman scoring a 0, 1, 2, 3, 4 or 6 runs. We then calculated the cumulative probabilities for each ball. Suppose we don't have sufficient data about a particular batsman-bowler pair (Note: Here we have kept a threshold of 5 below which we need clustering) we use the cluster probabilities.

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage2/frontend.png?raw=true" alt="Front end" width="400" height="300">

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage2/simulated.png?raw=true" alt="Simulation" width="300" height="285">

For wicket probability we started with a probability of 0.9 and then calculated the probability such that this probability decreases after each ball and once this probability falls below 0.5 we say that a wicket is taken. We then simulated this for 6 matches and obtained the results for these.

### PHASE 3 : DECISION TREE SIMULATION

This phase involves the building of a decision tree for match simulation. The important part in building a decision tree is to make the input suitable to be passed into the decision tree. We calculated the average strike rate, average economy for every cluster so as to be able to obtain the data relevant for this training. Here are the 2 visualizations for Decision trees.

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage3/above.png?raw=true" alt="Decision tree for runs" width="500" height="400">


The top one indicates the Decision tree for runs and the bottom one indicates the decision tree for the wickets. This input data was converted to LabeledPoint (an input form suitable for decision tree) and then fed into the decision tree. We then trained this decision tree and then simulated this for 10 matches and noted the outcomes.

<img src="https://github.com/sumanthvrao/IPL-Spark-Analysis/blob/master/stage3/below.png?raw=true" alt="Decision tree for wickets" width="500" height="400">

### Authors

- Siddharth Itagi
- Sumanth V Rao
- Sumedh Bhasarkod
- Tanmaya Udupa
