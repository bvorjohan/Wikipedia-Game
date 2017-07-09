import tf_idf
import Scraper
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

'''
reference:
http://colah.github.io/posts/2015-08-Understanding-LSTMs/
http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
http://www.wildml.com/2016/07/deep-learning-for-chatbots-2-retrieval-based-model-tensorflow/
http://blog.christianperone.com/2011/09/machine-learning-text-feature-extraction-tf-idf-part-i/



'''





beginning_url = "https://en.wikipedia.org/wiki/Trigonometry"
end_url = "https://en.wikipedia.org/wiki/Abraham_Lincoln"

def Wikipediaize(url):
    try:
        return "https://en.wikipedia.org"+url
    except:
        return "https://en.wikipedia.org"

# obtain seed and target pages
seed_text = Scraper.get_text(end_url)
# vocabulary = set(seed_text)
# print(len(vocabulary))

# debug first text

# vectorize target, use in predictor
vectorizer = TfidfVectorizer()
# print(seed_text)
vectorizer.fit([seed_text])
print()
print(vectorizer.idf_[vectorizer.vocabulary_["how"]])
matr = vectorizer.transform([Scraper.get_text(beginning_url)])

word_in_question = "most"
print(word_in_question,matr[(0,vectorizer.vocabulary_[word_in_question])])
end_matrix = vectorizer.transform([seed_text])
# print(matr)
# print(matr2)
# print(np.dot(matr,matr2.T).todense())
# print(np.dot(matr2,matr2.T).todense())
# print(vectorizer.vocabulary)
# print(vectorizer.stop_words_)
# for loop; max value = 20?
active_url = beginning_url
winner = ""
steps = [beginning_url]
print("Runnin....")
for _ in range(20):
    urls = Scraper.get_links(active_url)
    tf_idf_vectors = {}
    most_similar_url = ""
    biggest_dot = 0
    count = 0
    if "/wiki/Abraham_Lincoln" in urls:
        print("U WIN OMGGGGGG")
        winner = "u my frand"
        break
    for url in urls:
        count += 1
        if count%10 == 0:
            print("Parsing URL " + str(count) + " out of " + str(len(urls)))
        if False:
            print("Parsing URL...")
            # print(url)
            print(Wikipediaize(url))
            print(end_url)
        if Wikipediaize(url) == end_url:
            print("U WIN OMG")
            break
        if url not in tf_idf_vectors:
            try:
                url_vector = vectorizer.transform([Scraper.get_text("https://en.wikipedia.org"+url)])
            except:
                pass
            else:
                dotted = np.dot(url_vector,end_matrix.T).todense()
                tf_idf_vectors[url] = dotted
                if False:
                    print("Similarity: "+str(dotted))
                if (dotted > biggest_dot):
                    biggest_dot = dotted
                    most_similar_url = url

    print("Winner: " + most_similar_url + " with value: " + str(biggest_dot))
    active_url = Wikipediaize(most_similar_url)
    steps.append(active_url)

if winner:
    print("YAY YOU WON!")
else:
    print("Aw nah")


    # process body text in seed; make list of urls
    # for each url in list of urls:
        # obtain body text in url
        # vectorize body text
        # dot product into score
    # find max score in vector
    # store corresponding url in map tracker
    # pass new url into loop

# return stuff
