from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x=4

# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
print(bisect_left(a,x))
# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
print(bisect_right(a,x))