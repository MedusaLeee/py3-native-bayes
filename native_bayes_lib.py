from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from data_set import *

post_list, class_list, test_list = load_data_set()

# 实例化CountVectorizer
tfidfVectorizer = TfidfVectorizer()

train_term_matrix = tfidfVectorizer.fit_transform(post_list)
# 注意，测试样本调用的是transform接口
test_term_matrix = tfidfVectorizer.transform(test_list)

# 调用MultinomialNB分类器
clf = MultinomialNB().fit(train_term_matrix, class_list)
doc_class_predicted = clf.predict(test_term_matrix)

print(doc_class_predicted)




