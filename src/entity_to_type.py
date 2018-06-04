import pandas as pd

typed_abstracts = "typed_abstracts"
entity_annotations = "annotated_abstracts"
load_file_with_types = "instance_types_2016_en.ttl"


df = pd.read_csv(load_file_with_types, header=None, delimiter="\s+", names = ["Subject", "Property", "Object", "Point"])
df = df.drop('Property', 1)
df = df.drop('Point', 1)

df = df.set_index('Subject')
# Remove duplicated types
df = df[~df.index.duplicated(keep='first')]
dictionary = df['Object'].to_dict()

with open(typed_abstracts, "w") as entity_type_file:
    with open(entity_annotations, "r") as abstract_file_with_entities:
            for line in abstract_file_with_entities:
                list_of_types_to_save = []
                entities = line.split(" ")

                for en in entities:
                    en = en.replace("\n", "")
                    try:
                        type = dictionary['<http://dbpedia.org/resource/' + en + '>']
                    except:
                        continue
                    type = type.replace(">", "")
                    type = type.replace("<http://dbpedia.org/ontology/", "")
                    type = type.replace("<http://www.w3.org/2002/07/", "")
                    list_of_types_to_save.append(type)
                final_sentence = " ".join(list_of_types_to_save).encode("utf-8")
                entity_type_file.write(final_sentence + "\n")