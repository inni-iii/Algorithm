#큐는 선입선출 구조이다. 스택과는 달리, 먼저 삽입된 원소부터 삭제된다.

from collections import deque

#큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #다음 출력을 위해 역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력. slice 사용 불가능


#result
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])

#혹시 deque 객체를 리스트 자료형으로 변경하고자 한다면, list() 메서드를 이용하자.
