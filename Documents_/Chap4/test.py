from nltk.tokenize import sent_tokenize

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')  # Có thể cần để nhận diện thực thể

text = "Xin chào. Đây là một bài kiểm tra."
print(sent_tokenize(text))
