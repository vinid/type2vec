import re
import spotlight


ROOT_FOLDER = ""

file_path = ROOT_FOLDER + "2016_data/abstracts_2016.ttl"

def annotate(string, conf= 0.5, supp = 0):
    """
    Wrapper around the annotation function provided by spotlight
    :param string:
    :return:
    """
    annotations = []
    try:
        annotations = spotlight.annotate('http://localhost:2222/rest/annotate',
        string,
        confidence = conf, support = supp)
    except:
        pass
    return annotations

with open(ROOT_FOLDER + "annotated_abstracts", "w") as text_file:
    with open(file_path, "r") as abstract:
        for line in abstract:
            text_saved_annotated = []
            text_to_be_annotated = re.findall('"([^"]*)"', line)[0] # to extract the actual abstract
            annotations = annotate(text_to_be_annotated)
            for k in annotations:
                text_saved_annotated.append(k["URI"].replace("http://dbpedia.org/resource/",""))
            final_sentence = " ".join(text_saved_annotated).encode("utf-8")
            text_file.write(final_sentence + "\n")





