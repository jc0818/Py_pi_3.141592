#WordCloud py Code.
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
# nltk stopwords 다운로드
nltk.download('stopwords')

# 뉴욕 타임즈 기사 기반. 24-05-31 기사 Biden Calls for End to Gaza War, Endorsing Israeli Cease-Fire Proposal 中
text = """
Declaring Hamas no longer capable of carrying out a major terrorist attack on Israel, President Biden said on Friday that it was time for a permanent cease-fire in Gaza and endorsed a new plan he said Israel had offered to win the release of hostages and end the fighting.
“It’s time for this war to end, for the day after to begin,” Mr. Biden said, speaking from the State Dining Room at the White House. He also gave a stark description of Hamas’s diminished capabilities after more than seven months of Israeli attacks, saying that “at this point, Hamas is no longer capable of carrying out another Oct. 7.”
“This is truly a decisive moment,” Mr. Biden said. “Israel has made their proposal. Hamas says it wants a cease-fire. This deal is an opportunity to prove whether they really mean it.”
With that statement, Mr. Biden appeared to be revealing his true agenda: making public elements of the proposal in an effort to pressure both Hamas and Israel to break out of a monthslong deadlock that has resulted in the killing of thousands of Palestinians.
American officials have described Hamas’s leader, Yahya Sinwar, as interested only in his own survival and that of his family and inner circle, as they presumably operate from tunnels deep under southern Gaza. But officials have also said Prime Minister Benjamin Netanyahu of Israel has little incentive to move to a real cease-fire, because of the widespread belief in Israel that as soon as the surviving hostages are returned, and a last cease-fire begins, he will most likely lose his fragile hold on power.
Mr. Biden’s remarks came at a pivotal moment in his re-election campaign, a day after his rival, former President Donald J. Trump, was convicted of 34 felony charges. At the same time, he has been facing growing pressure at home over the bloodshed in Gaza, which has led to eruptions on college campuses and on the streets of American cities, and alienated many of his own supporters.
Mr. Biden described the three-phase Israeli plan as a “comprehensive new proposal” that amounted to a road map to an “enduring cease-fire.” But at several moments in the past few months, Mr. Netanyahu has directly contradicted Mr. Biden. And so far Hamas has never accepted a comprehensive proposal, declaring in its public statements that fighting must end before major hostage releases or any agreement with Israel.
Smoke rising after an Israeli strike in the southern Gaza city of Rafah on Friday.Credit...Eyad Baba/Agence France-Presse — Getty Images
Hints of differences came almost as soon as Mr. Biden finished speaking. Following his speech, the Israeli Prime Minister’s Office said the Israeli government was “united in the desire to bring home our hostages as soon as possible.”

"""
# 텍스트 정제
text = re.sub(r'\W+', ' ', text.lower())
# 불용어 설정 및 제거
stop_words = set(stopwords.words('english'))
words = text.split()
words = [word for word in words if word not in stop_words]
# 단어 빈도 계산
word_counts = Counter(words)
# 빈출 단어 순위 5개 추출
most_common_words = word_counts.most_common(5)
most_common_words_dict = dict(most_common_words)
# 빈출 단어 역순 5개 추출
least_common_words = word_counts.most_common()[:-6:-1]
least_common_words_dict = dict(least_common_words)
# 워드 클라우드 생성 함수
def generate_wordcloud(word_freq, title):
    wordcloud = WordCloud(background_color='white', width=800, height=600).generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()
# 빈출 단어 순위 5개 워드 클라우드
generate_wordcloud(most_common_words_dict, "Top 5 Most Frequent Words")

# 빈출 단어 역순 5개 워드 클라우드
generate_wordcloud(least_common_words_dict, "Top 5 Least Frequent Words")
