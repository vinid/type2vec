# Type Vector Representations from Text

This repository contains the code and the models for the Type 2 Vec (T2V) algorithm [1], an approach to embed ontological types
of a knowledge graph into the vector space using a distributional approach.

Details on the original model are in [2] and [here](https://github.com/vinid/entity2vec) you can find the respective 
code.

## Datasets
Gold Standard on Analogies can be found in the data folder.

## Code
We supply the scripts that can be used to generate the embeddings. It is necessary to download the abstracts and the entity-type link from DBpedia.

+ [Link to DBpedia Dumps](https://wiki.dbpedia.org/dbpedia-version-2016-04)
+ [Link to Abstracts](http://downloads.dbpedia.org/2016-04/core/long_abstracts_en.ttl.bz2)
+ [Link to Instance Type](http://downloads.dbpedia.org/2016-04/core/instance_types_en.ttl.bz2)

## Models
Models that can be used to repeat the experiments can be downloaded from [here](http://inside.disco.unimib.it/download/federico/type2vec/). These models can be loaded using the Gensim python package.

## Other Software
You can easily install the software for evaluating topological measures is [here](https://github.com/gsi-upm/sematch). Sematch was used to run the experiments related to the comparison with similarity measures on the ontology.

## References

[1] [F. Bianchi, M. Soto, M. Palmonari, and V. Cutrona, “Type Vector Representations from Text: An empirical analysis” in Deep Learning for Knowledge Graphs and Semantic Technologies Workshop, co-located with the Extended Semantic Web Conference, 2018.](http://ceur-ws.org/Vol-2106/paper9.pdf)
