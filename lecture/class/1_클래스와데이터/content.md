# 클래스가 필요한 이유
지금까지 배운 것을 토대로 문제를 풀어보자.

## 문제: 학생 정보 출력 프로그램 만들기
당신은 두 명의 학생 정보를 출력하는 프로그램을 작성해야 한다. 각 학생은 이름, 나이, 성적을 가지고 있다.
* 요구 사항:
1. 첫 번째 학생의 이름은 "학생1", 나이는 15, 성적은 90입니다.
2. 두 번째 학생의 이름은 "학생2", 나이는 16, 성적은 80입니다.
3. 각 학생의 정보를 다음과 같은 형식으로 출력해야 합니다: "이름: [이름] 나이: [나이] 성적: [성적]"
4. 변수를 사용해서 학생 정보를 저장하고 변수를 사용해서 학생 정보를 출력해야 합니다.

예시 출력: 
```
이름: 학생1 나이: 15 성적: 90
이름: 학생2 나이: 16 성적: 80
```

정답:**ClassStart1.py**
```python
def main():
    student1_name = "학생1"
    student1_age = 15
    student1_grade = 90

    student2_name = "학생2"
    student2_age = 16
    student2_grade = 80

    print(f"이름: {student1_name} 나이: {student1_age} 성적: {student1_grade}")
    print(f"이름: {student2_name} 나이: {student2_age} 성적: {student2_grade}")

if __name__ == "__main__":
    main()

```
* 학생 2명을 다루어야 하기 때문에 각각 다른 변수를 사용했다. 
* 이 코드의 문제는 학생이 늘어날 때 마다 변수를 추가로
선언해야 하고, 또 출력하는 코드도 추가해야 한다.
* 이런 문제를 어떻게 해결할 수 있을까? 앞서 배운 배열을 사용하면 문제를 해결할 수 있다.

## 문제: 이전 문제에 배열을 사용하자
이전 문제에 배열을 적용하자. 
그래서 학생이 추가되어도 코드 변경을 최소화 해보자.

```python
def main():
    student_names = ["학생1", "학생2"]
    student_ages = [15, 16]
    student_grades = [90, 80]

    for i in range(len(student_names)):
        print(f"이름: {student_names[i]} 나이: {student_ages[i]} 성적: {student_grades[i]}")

if __name__ == "__main__":
    main()

```
* 배열을 사용한 덕분에 학생이 추가되어도 배열에 학생의 데이터만 추가하면 된다. 
* 이제 변수를 더 추가하지 않아도 되고, 출력 부분의 코드도 그대로 유지할 수 있다.

**학생 추가 전**
```python
student_names = ["학생1", "학생2"]
student_ages = [15, 16]
student_grades = [90, 80]

```

**학생 추가 후**
```python
student_names = ["학생1", "학생2", "학생3", "학생4", "학생5"]
student_ages = [15, 16, 17, 10, 16]
student_grades = [90, 80, 100, 80, 50]
```

## 배열 사용의 한계
* 배열을 사용해서 코드 변경을 최소화하는데는 성공했지만, 한 학생의 데이터가 studentNames ,studentAges ,studentGrades 라는 3개의 배열에 나누어져 있다. 
* 따라서 데이터를 변경할 때 매우 조심해서 작업해야 한다. 
* 예를 들어서 학생 2의 데이터를 제거하려면 각각의 배열마다 학생2의 요소를 정확하게 찾아서 제거해주어야 한다

**학생2제거**
```python
student_names = ["학생1", "학생3", "학생4", "학생5"]
student_ages = [15, 17, 10, 16]
student_grades = [90, 100, 80, 50]
```

## 클래스 도입
* 앞서 이야기한 문제를 클래스를 도입해서 해결해보자.
* 클래스를 사용해서 학생이라는 개념을 만들고, 각각의 학생 별로 본인의 이름, 나이, 성적을 관리하는 것이다.
* 우선 코드를 작성하고 실행해보자.

**Student 클래스**
```python
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = 0

```
* class 키워드를 사용해서 학생 클래스( Student )를 정의한다. 학생 클래스는 내부에 이름( name ), 나이( age ), 성적( grade ) 변수를 가진다.
* 이렇게 클래스에 정의한 변수들을 인스턴스 변수라 한다.
* 클래스는 관례상 대문자로 시작하고 낙타 표기법을 사용한다  
* * 예): Student , User , MemberService 

이제 학생 클래스를 사용하는 코드를 작성해보자.

**ClassStart3**
```python
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = 0

def main():
    student1 = Student()
    student1.name = "학생1"
    student1.age = 15
    student1.grade = 90

    student2 = Student()
    student2.name = "학생2"
    student2.age = 16
    student2.grade = 80

    print(f"이름: {student1.name} 나이: {student1.age} 성적: {student1.grade}")
    print(f"이름: {student2.name} 나이: {student2.age} 성적: {student2.grade}")

if __name__ == "__main__":
    main()

```

**실행 결과**
```
이름:학생1 나이:15 성적:90
이름:학생2 나이:16 성적:80
```

**클래스와 사용자 정의 타입**

* 타입은 데이터의 종류나 형태를 나타낸다.
* int 라고 하면 정수 타입, str 이라고 하면 문자 타입이다.
* 학생( Student )이라는 타입을 만들면 되지 않을까?
* 클래스를 사용하면 int , str 과 같은 타입을 직접 만들 수 있다.
* 사용자가 직접 정의하는 사용자 정의 타입을 만들려면 설계도가 필요하다. 이 설계도가 바로 클래스이다.
* 설계도인 클래스를 사용해서 실제 메모리에 만들어진 실체를 객체 또는 인스턴스라 한다.
* 클래스를 통해서 사용자가 원하는 종류의 데이터 타입을 마음껏 정의할 수 있다.
> 용어: 클래스, 객체, 인스턴스
>* 클래스는 설계도이고, 이 설계도를 기반으로 실제 메모리에 만들어진 실체를 객체 또는 인스턴스라 한다. 
>* 둘다 같은 의미로 사용된다.
>* 여기서는 학생( Student ) 클래스를 기반으로 학생1( student1 ), 학생2( student2 ) 객체 또는 인스턴스를 만들었다.

> 코드 분석
* 변수 선언
* 객체 생성
* 참조값 보관
* 객체 값 사용 
    * 객체 값 대입 => 주소접근->변수접근->대입
    * 객체 값 읽기 => 주소접근->변수접근
```python
student1 = Student()
student2 = Student()
student1 = student2

print(id(student1))
print(id(student2))

#객체 값 대입
student1.name = "학생1"
student1.age = 15
student1.grade = 90
#객체 값 사용
print(f"이름: {student1.name} 나이: {student1.age} 성적: {student1.grade}")

```

# 배열 도입
* 클래스와 객체 덕분에 학생 데이터를 구조적으로 이해하기 쉽게 변경할 수 있었다.
* 마치 실제 학생이 있고, 그 안에 각 학생의 정보가 있는 것 같다. 따라서 사람이 이해하기도 편리하다.
* 이제 각각의 학생 별로 객체를 생성하고, 해당 객체에 학생의 데이터를 관리하면 된다.
* 하지만 코드를 보면 아쉬운 부분이 있는데, 바로 학생을 출력하는 부분이다.
* 새로운 학생이 추가될 때 마다 출력하는 부분도 함께 추가해야 한다.
```python
print(f"이름: {student1.name} 나이: {student1.age} 성적: {student1.grade}")
print(f"이름: {student2.name} 나이: {student2.age} 성적: {student2.grade}")

```
* 배열을 사용하면 특정 타입을 연속한 데이터 구조로 묶어서 편리하게 관리할 수 있다.
* Student 클래스를 사용한 변수들도 Student 타입이기 때문에 학생도 배열을 사용해서 하나의 데이터 구조로 묶어
서 관리할 수 있다.
* Student 타입을 사용하는 배열을 도입해보자.

**ClassStart4**
```python
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = 0

def main():
    student1 = Student()
    student1.name = "학생1"
    student1.age = 15
    student1.grade = 90

    student2 = Student()
    student2.name = "학생2"
    student2.age = 16
    student2.grade = 80

    students = [student1, student2]

    print(f"이름: {students[0].name} 나이: {students[0].age} 성적: {students[0].grade}")
    print(f"이름: {students[1].name} 나이: {students[1].age} 성적: {students[1].grade}")

if __name__ == "__main__":
    main()

```

코드를 분석해보자
* 배열에 참조값 대입
    * 대입은 항상 변수에 있는 값을 복사한다.
```python
students = [student1, student2]
```
![image](https:#github.com/mtak0235/TIL/assets/48946398/a7136312-7509-4a5c-b3bb-0b18401ec718)
*  변수에는 인스턴스 자체가 들어있는 것이 아니다! 인스턴스의 위치를 가리키는 참조값이 들어있을 뿐이다! 따라서 대입 ( = )시에 인스턴스가 복사되는 것이 아니라 참조값만 복사된다.
# 배열 도입- 리팩토링
배열을 사용한 덕분에 출력에서 다음과 같이 for문을 도입할 수 있게 되었다.
```python
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = 0

def main():
    student1 = Student()
    student1.name = "학생1"
    student1.age = 15
    student1.grade = 90

    student2 = Student()
    student2.name = "학생2"
    student2.age = 16
    student2.grade = 80

    # 배열 선언 및 초기화
    students = [student1, student2]

    # for 루프 적용
    for student in students:
        print(f"이름: {student.name} 나이: {student.age} 성적: {student.grade}")

if __name__ == "__main__":
    main()

```

# 문제: 영화 리뷰 관리하기1
* 문제 설명
* 당신은 영화 리뷰 정보를 관리하려고 한다. 
* 먼저, 영화 리뷰 정보를 담을 수 있는 MovieReview 클래스를 만들어보자.

* 요구 사항
1. MovieReview 클래스는 다음과 같은 멤버 변수를 포함해야 한다.
영화 제목 ( title )
리뷰 내용 ( review )
2. MovieReviewMain 클래스 안에 main() 메서드를 포함하여, 영화 리뷰 정보를 선언하고 출력하자.
* 예시 코드 구조 
```python
class MovieReview:
    def __init__(self):
        self.title = ""
        self.review = ""
```
* 출력 예시 
```
영화 제목: "인셉션", 리뷰: "인생은 무한 루프"
영화 제목: "어바웃 타임", 리뷰: "인생 시간 영화!" 
```

# 문제: 영화 리뷰 관리하기2
기존 문제에 배열을 도입하고, 영화 리뷰를 배열에 관리하자.
리뷰를 출력할 때 배열과 for 문을 사용해서 print를 한번만 사용하자

# 문제: 상품 주문 시스템 개발
* 문제 설명
* 당신은 온라인 상점의 주문 관리 시스템을 만들려고 한다.
먼저, 상품 주문 정보를 담을 수 있는 ProductOrder 클래스를 만들어보자.
* 요구 사항
1. ProductOrder 클래스는 다음과 같은 멤버 변수를 포함해야 한다.
상품명 ( productName )
가격 ( price )
주문 수량 ( quantity )
2. ProductOrderMain 클래스 안에 main() 메서드를 포함하여, 여러 상품의 주문 정보를 배열로 관리하고, 그
정보들을 출력하고, 최종 결제 금액을 계산하여 출력하자.
3. 출력 예시와 같도록 출력하면 된다.
* 예시 코드 구조 
```python
class ProductOrder:
    def __init__(self):
        self.productName = ""
        self.price = 0
        self.quantity = 0

```
```python
def main():
 # 여러 상품의 주문 정보를 담는 배열 생성
 # 상품 주문 정보를 `ProductOrder` 타입의 변수로 받아 저장
 # 상품 주문 정보와 최종 금액 출력
```
출력 예시
```
상품명: 두부, 가격: 2000, 수량: 2
상품명: 김치, 가격: 5000, 수량: 1
상품명: 콜라, 가격: 1500, 수량: 2
총 결제 금액: 12000
```