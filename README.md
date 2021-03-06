## Traversing the Trump Twitterverse: A social network analysis.   
Repo and [blog post](https://jonkislin.github.io/2018/04/04/traverse.html) are works in progress.  
Inspired by Tim Martin's [Promoting Positive Climate Change Conversations via Twitter](https://zeromh.github.io/climate_change_conversations/)

__Question__: Given a large sample of tweets referencing "@realDonaldTrump," can we generate a graph network such that distinct [communities](http://senseable.mit.edu/community_detection/), [moderators](https://www.geeksforgeeks.org/betweenness-centrality-centrality-measure/), and [influencers](https://en.wikipedia.org/wiki/PageRank) are identifiable?  
__Data Collection__: Queried the Twitter streaming API for any tweets including @realDonaldTrump. Stored in mongoDB.  
__Data Analysis__: Pyspark, Spark SQL, networkX, python-louvain (community) package, LDA topic modeling.  

__Conclusions__: 
* Communities are fairly clean: clear pro-Donald Trump and anti-Donald Trump communities, especially when Trump and his connections to other users are removed from the graph. 
* Influencers: news organizations
* Moderators: also news organizations... and [Ted Lieu](https://lieu.house.gov)?

__Visualizations__
* Check out [package manager / code galaxies by Andrei Kashcha](https://github.com/anvaka/pm)
* Web-hosted demo with current project data in works.

__Machines used__:  
* Macbook Pro 13" (2015)
* Amazon c5.9xlarge EC2 instance (36 cores, 68 GB RAM) with Spark (single node)

_March - April 2018_
