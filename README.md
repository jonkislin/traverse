# traverse
Traversing the Trump Twitterverse: A social network analysis. March 2018
Repo and [blog post](https://jonkislin.github.io/2018/04/04/traverse.html) are works in progress.

Inspired by Tim Martin's [Promoting Positive Climate Change Conversations via Twitter](https://zeromh.github.io/climate_change_conversations/)

#### Question: 
Given a large sample of tweets referencing "@realDonaldTrump," can we generate a graph network such that distinct [communities](http://senseable.mit.edu/community_detection/), [moderators](https://www.geeksforgeeks.org/betweenness-centrality-centrality-measure/), and [influencers](https://en.wikipedia.org/wiki/PageRank) are identifiable?

#### Data Collection: 
Queried the Twitter streaming API for any tweets including @realDonaldTrump. Entered into an Amazon EC2 hosted mongoDB database in real-time.

#### Data Analysis: 
Pyspark, Spark SQL, networkX, python-louvain (community) package, LDA topic modeling.

#### Conclusions: 
* Communities are fairly clean: clear pro-Donald Trump and anti-Donald Trump communities, especially when Trump and his connections to other users are removed from the graph. 
* Influencers: news organizations
* Moderators: also news organizations... and [Ted Lieu](https://lieu.house.gov)?
