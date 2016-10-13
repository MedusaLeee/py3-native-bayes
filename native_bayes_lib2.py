from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from data_set import *

post_list, class_list, test_list = load_data_set()

# 实例化CountVectorizer
train_tfidfVectorizer = TfidfVectorizer()

train_term_matrix = train_tfidfVectorizer.fit_transform(post_list)
vocabulary = train_tfidfVectorizer.vocabulary_
# 如果实例化的测试集的TfidfVectorizer必须使用和训练集一样的词袋vocabulary
test_tfidfVectorizer = TfidfVectorizer(vocabulary=vocabulary)

test_term_matrix = test_tfidfVectorizer.fit_transform(test_list)

# 调用MultinomialNB分类器
clf = MultinomialNB(alpha=0.001).fit(train_term_matrix, class_list)
doc_class_predicted = clf.predict(test_term_matrix)

print(doc_class_predicted)




