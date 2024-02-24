# class

## class definition
Python có sẵn nhiều function, như len, print, type, sum, min, max ... nhưng
rõ ràng là không đủ và cung cấp cách để người dùng tự tạo các function của chính mình
với từ khoá def:

```python
def double(x):
    return x + x
```

Tương tự với lý lẽ đó, Python có sẵn nhiều kiểu dữ liệu như int, float, string, bool,
list, tuple, dict, set,... nhưng cũng là không đủ nên cung cấp cho người dùng cách để
tự tạo kiểu dữ liệu mới với từ khoá class:

```python
class Student():
    def __init__(self, name, a):
        self.name = name
        self.age = a
        self.location = 'VietNam'
```


code trên định nghĩa 1 kiểu dữ liệu mới: kiểu Student.
Từ "class" và từ "kiểu" có thể dùng thay nhau khi nói.

Như khi học các kiểu dữ liệu có sẵn của Python, ta hay nói x = 5
thì x có kiểu int vì:

```python
>>> x = 5
>>> print(type(x))
<class 'int'>
```

Chú ý chữ "class" trước 'int', thay vì nói x là kiểu int, ta có thể nói:
- x (hay 5) là 1 int object
- x là 1 instance của class int (cách này ít dùng hơn nhưng sẽ hay thấy trong tài liệu trên trang chủ Python)

Code sau đây sẽ tạo 1 Student object:

```python
>>> p = Student('Py', 18)
>>> print(p)
<__main__.Student object at 0xe456b70deb0>
>>> print(p.name, p.age, p.location)
Py 18 VietNam
```

Cú pháp `TênClass(argument)` cũng dùng dấu `()` như khi gọi 1 function.
Tên của class thường viết hoa chữ cái ĐầuTiên - đây là quy ước trong PEP8
 (trừ các kiểu dữ liệu có sẵn của Python int float list ...).

Chú ý số đầu vào (argument) ở đây là 2, mặc dù trong `__init__` ta ghi 3 arguments:
`self, name, a`. Khi định nghĩa 1 function trong class (gọi là 1 method),
luôn luôn phải thêm argument đầu tiên `self`,
`self` đại diện cho object SẼ được tạo ra, nếu cảm thấy khó hiểu, cứ làm đúng
"luôn thêm self" là được. Khi gọi method thì không cần đưa self vào:

```python
class Student():
    def __init__(self, name, a):
        self.name = name
        self.age = a
        self.location = 'VietNam'
    def hello(self):
        print("{} nói hello".format(self.name))
>>> p = Student('Py', 18)
>>> p.hello()
Py nói hello
```

Chú ý method đặc biệt `__init__` có 2 dấu `_` ở trước và 2 dấu `_` ở sau chữ init,
các method trong Python có tên với cặp 2 dấu `_` trước sau gọi là `dunder method`
(double underscore method). Những method này đóng vai trò đặc biệt trong Python,
và tên đã được quy ước sẵn. Như `__init__` ở đây sẽ được goi khi ta tạo 1 object
với `Student('Pymier', 18)`.
Cách tốt nhất Pymi biết để làm quen với cú pháp tạo class mới là
gõ đi gõ lại 100 lần (nghiêm túc!),
dần bạn sẽ quen và không còn thấy lạ nữa.


Khi tạo 1 số kiểu int, ta thường viết x = 5, nhưng dùng cú pháp class hoàn toàn được:

```python
>>> int(5)
5
>>> int('5')
5
```

Đến đây, sau khi đã biết tự tạo 1 class, cần nhìn kỹ lại "class để làm gì".
Class là 1 cơ chế để gộp dữ liệu (name, age, location trong ví dụ), và các
methods (hello) thành 1 khối.

Trong Python, hoàn toàn có thể không tạo class mới vẫn code bình thường,
bằng chứng là bạn đã học đến bài này, làm đủ loại bài tập mà không 1 lần
tạo class mới. Bởi thay vì dùng class để gộp data và method, ta hoàn toàn
có thể dùng 1 dictionary hay 1 list để chứa data, và định nghĩa function để
xử lý data.

Dùng class là 1 cách làm khác, tương đương với cách ta vẫn làm từ đầu đến
giờ (dict/list + function) chứ không phải thứ gì mới có khả năng hơn, chỉ đơn
thuần là 1 cách làm khác. Như ta có thể nấu mì tôm bằng xoong, hoặc bằng
ấm đun nước, chỉ là cách làm khác nhau, kết quả gần giống nhau chứ không
có cái nào có gì hơn đột phá.

### class inheritance
Khái niệm này đưa ra 1 cơ chế "đột phá", tạo ra sự khác biệt khi dùng class.

inheritance có nghĩa tiếng Việt là "kế thừa", kế thừa là chuyện con
thừa hưởng những tính chất và khả năng của bố mẹ (trong sinh học), bố mẹ
có đặc điểm gì, thì con có đặc điểm/khả năng đó.

Trong lập trình, kế thừa 1 class sẽ khiến class mới được thừa hưởng MỌI
tính chất của class mà nó kế thừa (gọi là base class/parent class).
Về bản chất, đây là 1 cơ chế "copy code tự động".

```python
class Py(Student):
    def code(self):
        print("{} can code Python!!!".format(self.name))
```

```python
>>> pm = Py("Pikachu", 18)
>>> pm.code()
Pikachu can code Python!!!
>>> pm.hello()
Pikachu nói hello
```

Dòng `class Py(Student)` là cú pháp để class Py kết thừa (inherit) mọi data attribute (thuộc tính) / method
của class Student ở trên. Ta thấy không cần phải gõ lại `__init__`, không cần `def hello` nhưng
pm hoạt động như 1 Student, và còn thêm method `code` mà Student không có.

Kế thừa được dùng rất nhiều, bởi nó giúp lập trình viên chỉ gõ 1 vài dòng tạo class mới đã
tự động "copy" được những gì class khác đã định sẵn.
- Chỉ với vài dòng code là có 1 chương trình có [giao diện đồ hoạ (GUI)](https://pp.pymi.vn/article/gui/)
nhờ kế thừa
- hay chỉ với vài trăm dòng đã có [game FlappyBird](https://github.com/TimoWilken/flappy-bird-pygame/blob/master/flappybird.py#L20)
- [Code Django dùng rất nhiều kế thừa](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)

Để kiểm tra 1 object có phải 1 kiểu nào không, dùng isinstance

```
>>> isinstance(pm, Py)
True
>>> isinstance(p, Py)
False
>>> isinstance(pm, Student)
True
```

Vì Py kế thừa Student nên pm cũng là 1 Student object (con của 2 con mèo vẫn là 1 con mèo).

### Inheritance in Python

Python sử dụng inheritance cho các exception, chú ý tên các Exception đều
viết hoa chữ cái đầu theo cách đặt tên class. Mối quan hệ giữa các exception:
class nào kế thừa class nào - tạo thành một cây gia phả (hierachy). Hierachy là
khái niệm mối quan hệ của các class khi dùng inheritance.

https://docs.python.org/3/library/exceptions.html#exception-hierarchy


### print object

```python
>>> p = Student('Py', 18)
>>> print(p)
<__main__.Student object at 0xe456b70deb0>
```

Khi print 1 object, nó hiện ra dòng "Student object at 0x..." tức object Student nằm ở
địa chỉ nào trên RAM. Output này không thực sự hữu ích với lập trình viên. Khi print(p),
ta có thể muốn thấy tên, tuổi của học viên này. Method đặc biệt: `__str__` sẽ trả
về 1 str, Python sẽ hiển thị nội dung đó khi print, hay nói cách khác, khi gõ print(p),
thực chất Python sẽ gọi `print(p.__str__())`:

```python
class Student():
    def __init__(self, name, a):
        self.name = name
        self.age = a
        self.location = 'VietNam'
    def __str__(self):
        return "Student {}, {} tuổi".format(self.name, self.age)
```

```python
>>> p = Student('Py', 18)
>>> print(p)
Student Py, 18 tuổi
```

Python có rất nhiều các dunder method khác, xem `dir(p)` để thấy đầy đủ.

### OOP

class là khái niệm xuất hiện trong một programming paradigm (tạm dịch là mô hình lập trình),
có tên "Object Oriented Programming", mô hình mà mọi thứ đều là các object, chúng sẽ
gọi các method để thực hiện các hành động, và tương tác lên nhau, tưởng tượng như
trong 1 game máy tính có nhiều người chơi cùng lúc, các nhân vật là các object tương tác với nhau.
OOP xuất hiện vào khoảng đầu những năm 90 của thế kỷ 20 (199x), phát minh bởi Alan Kay, trong
ngôn ngữ lập trình Smalltalk(https://squeak.org/) SmallTalk không thành công về mặt thương mại và
bị chiếm thị phần bởi Java, sau đó là C#, C++ đều dùng OOP rất nhiều.
Mô hình OOP rất phù hợp với 1 số bài toán (như game), nhưng không phù hợp với MỌI bài toán.
Các mô hình lập trình khác cũng phổ biến, không dùng OOP như:
- Procedure programming: C
- Functional programming: LISP, Ocaml, Haskell, Clojure, F#, Erlang, Elixir...
- Declarative programming: SQL, Prolog,...

Vậy Python nằm ở đâu? Các ngôn ngữ lập trình ban đầu đều rất "thuần khiết",
những sau quá trình phát triển nhiều năm đã mượn các khái niệm từ các
ngôn ngữ lập trình khác về, khiến chúng có thể xếp cả vào 3 nhóm OOP/procedure/functional
đều được: Python, Ruby, PHP, JavaScript...

Đọc thêm các paradigm tại:
https://en.wikipedia.org/wiki/Comparison_of_programming_paradigms


Tham khảo: https://docs.python.org/3/tutorial/classes.html
