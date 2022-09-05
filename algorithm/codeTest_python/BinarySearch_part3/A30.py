def match_wq(word,query):
  length=len(word)
  for i in range(length):
    if query[i]=='?':
      continue
    elif query[i]!=word[i]:
      return False
  return True


def solution(words, queries):
    answer = []
    # 중복 단어를 제거
    s=set(words)
    # 쿼리를 개별 진행
    for query in queries:
        count = 0 # 매치되는 경우
        for word in s:
            # 글자 수가 맞고 일치 할 경우
            if len(word)==len(query) and match_wq(word,query):
              count+=1
        answer.append(count)
    return answer

words=["frodo","front","frost","frozen","frame","kakao"]
queries=["fro??","????o","fr???","fro???","pro?"]

print(solution(words,queries))