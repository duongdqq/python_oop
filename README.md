# python_oop
### link 1 https://o7planning.org/vi/11415/lop-va-doi-tuong-trong-python
### link 2 https://phocode.com/python/python-huong-doi-tuong-trong-python/
1. Một số khái niệm
- Class: là một kiểu dữ liệu người dùng tự định nghĩa,tập hợp nhiều thuộc tính (attribute) và phương thuwcs (method) đặc trưng cho mọi đối tượng được tạo ra từ lớp đó
- Object: là một thể hiện cụ thể (thực thể) của CTDL được định nghĩa trong lớp. Mỗi object bao gồm cả biến thành viên và phương thức. Ví dụ list, tuple, dictionary, string, int là các class. Khi khai báo biến thuộc các lớp này thì chúng là các object
- Data member: là biến được định nghĩa trong class hoặc object
- Method: là hàm được định nghĩa trong class nhằm thực hiện 1 công việc cụ thể
- Inheritace: là một tính chất của các ngôn ngữ OOP cho phép các class kế thừa các đặc trưng của lớp được kế thừa

2. Cách tạo class
- Cú pháp class classname:
- Dòng đầu sử dụng string để mô tả ngắn gọn về class (không bắt buộc) 
  + Truy cập chuỗi này thông qua classname.__doc__
- Trong phần thân khai báo attribute (thuộc tính), method (phương thức) và constructor (phương thức khởi tạo)

3. Attribute
- Attribute là thuộc tính của lớp
- VD hình chữ nhật có 2 thuộc tính là width và height

4. Method
- Method là 1 hàm thông thường, nhưng là 1 hàm của class, nằm bên trong class
- Để sử dụng Method cần gọi thông qua Object
- Tham số đầu tiên của Method luôn là self

5. Constructor
- Là phương thức khởi tạo. Là một method đặc biệt của class, nó luôn có tên là '__init__'
- Tham số đầu tiên của constructor luôn là self
- Constructor được dùng để tạo ra một object
- Constructor gán giá trị từ tham số vào các attribute của object sẽ được tạo ra
- Có thể định nghĩa nhiều nhất 1 constructor trong class
- Nếu class không được định nghĩa constructor, python mặc định coi rằng nó kế thừa từ constructor của lớp cha
- Trong python, một số hàm trong class sẽ tự động được gọi khi ta khai báo 1 

6. Tạo object từ một class
- Khi tạo một object của class, constructor sẽ được gọi để tạo 1 object, các attribute của object sẽ được gán giá trị từ tham số
7. Tham số mặc định trong constructor
- Tất cả các tham số bắt buộc phải đặt trước tham số mặc định

8. So sánh các đối tượng
- Khi tạo 1 object thông qua constructor, sẽ có 1 thực thể được tạo ra nằm trên bộ nhớ có địa chỉ xác định
- Phép gán  cho BB không tạo ra thêm thực thể trên bộ nhớ, chỉ là trỏ địa chỉ AA tới BB 
- Toán tử == dùng để so sánh địa chỉ 2 đối tượng trỏ đến, trả về True nếu cả 2 đối tượng cùng trỏ tới cùng một địa chỉ trên bộ nhớ

9. Attribute
- Các object được tạo từ cùng 1 class sẽ nằm tại các địa chỉ khác nhau trên bộ nhớ
- Các attribute cùng tên cũng có các địa chỉ khác nhau trên bộ nhớ
- Python cho phép tạo 1 attribute mới cho 1 object cho trước
- Có thể gán giá trị cho các thuộc tính và khai báo thuộc tính mới ở bất cứ đâu sau phần định nghĩa lớp chứ không chỉ riêng bên trong phương thức khởi tạo.
- Thuộc tính được khai báo bên trong constructor __init__ được gọi là thuộc tính đối tượng
- Thuộc tính được khai báo bên trong class nhưng ngoài constructor __init__ được gọi là thuộc tính lớp. 
- Thuộc tính lớp được chia sẻ chung cho mọi đối tượng của lớp đó. Thuộc tính đối tượng chỉ dành riêng cho đối tượng
- Có 2 cách truy xuất thuộc tính lớp. 1, thông qua tên lớp. 2, thông qua thuộc tính đặc biệt __class__

10. Các hàm truy cập vào attribute
- Thông thường, truy cập vào attribute của 1 class qua toán tử 'dấu chấm'
- Tuy nhiên, python cho phép truy cập thông qua function
+ getattr(obj, name[, default])
+ hasattr(obj,name)
+ setattr(obj,name,value)
+ delattr(obj, name)

11. Các attribute có sẵn của class
- __dict__
- __doc__
- __class__
- __module__

12. Biến của lớp
- Được truy cập thông qua tên class hoặc object
- Nên truy cập biến của lớp thông qua tên lớp thay vì đối tượng để tránh nhầm lẫn giữa biến của lớp và thuộc tính
- Mỗi biến của lớp có 1 địa chỉ nằm trên memory và chia sẻ cho mọi đối tượng

13. Liệt kê danh sách các thành viên 
- Python cung cấp cho bạn hàm dir, hàm này liệt kê ra danh sách các phương thức, thuộc tính, biến của lớp hoặc của đối tượng.

14. Các tính chất của OOP trong Python
- Abstraction
- Polymorphism
- Encapsulation
- Inheritance

15. Self
- Bất kỳ method nào của Python đều phải có tham số self đầu tiên rồi mới đến các tham số khác
- self thực ra là biến đối tượng đã gọi method này
- Không trực tiếp đưa tham số self vào mà chỉ đưa các tham số thứ 2 trở đi. self được tự động thêm vào bởi trình thông dịch
16. Inheritance

- Kế thừa là định nghĩa một lớp dựa trên một lớp đã được định nghĩa trước đó. 
- Lớp kế thừa từ lớp khác được gọi là lớp dẫn xuất, lớp được các lớp khác kế thừa mình thì gọi là lớp cơ sở. 
- Kế thừa trong lập trình hướng đối tượng cho phép sử dụng lại mã nguồn và giảm độ phức tạp của chương trình
- Lớp dẫn xuất có thể kế thừa hoặc mở rộng các tính năng của lớp cơ sở
- Lớp dẫn xuất có thể thừa hưởng method của lớp cơ sở và có các method riêng. Ngoài ra còn có thể kế thừa và thay đổi method của lớp cơ sở. 
- Để kế thừa một lớp thì chúng ta đặt tên lớp đó bên trong cặp dấu ngoặc tròn () ngay phía sau phần định nghĩa tên lớp
- Nếu bên trong lớp cơ sở đã định nghĩa phương thức __init__(), chúng ta phải gọi lại phương thức __init__() từ lớp cơ sở.

17. Polymorphism
- Đa hình là có thể sử dụng các toán tử hay các hàm trên nhiều kiểu dữ liệu khác nhau.
- Bản thân các hàm có sẵn trong Python cũng có tính chất đa hình. 
- Chẳng hạn như hàm print() mỗi lần gọi hàm này có thể đưa vào hầu hết các kiểu dữ liệu khác nhau.
- 2 hoặc nhiều lớp dấn xuất có thể được định nghĩa bằng việc kế thừa từ 1 lớp cơ sở. Do các lớp dẫn xuất đều kế thừa 1 method của lớp cơ sở nhưng mỗi lớp có thể xuất ra các kết quả khác nhau

18. Các phương thức đặc biệt
- Tất cả các lớp dù là có sẵn hay do chúng ta định nghĩa đều kế thừa từ một lớp gốc trong Python có tên là object. 
- Lớp này có sẵn một số phương thức và đương nhiên là các lớp do chúng ta định nghĩa đều kế thừa các phương thức này
- ví dụ như phương thức __init__() 
- Trong Python khi chúng ta gọi đến các hàm hay toán tử được xây dựng sẵn như print(), del… chúng sẽ gọi đến các phương thức gốc của lớp object
- Chính vì các lớp do chúng ta định nghĩa đều được kế thừa từ lớp object nên chúng ta cũng có thể dùng các hàm hay toán tử có sẵn trong Python với các lớp của chúng ta. 
- Trong các ngôn ngữ như C++ thì tính chất này được gọi là quá tải toán tử (operator overloading).
- Một số phương thức được kế thừa từ lớp object là
  - init
  - str
  - len
  - del 
  
### link 3 https://www.howkteam.vn/course/lap-trinh-huong-doi-tuong-voi-python/lop-va-doi-tuong-trong-lap-trinh-huong-doi-tuong-voi-python-3877
1. Lớp và đối tượng trong lập trình hướng đối tượng với Python
- <__main__.SieuNhan object at 0x0106CD10> có nghĩa là sieu_nhan_A là đối tượng thuộc lớp SieuNhan ở hàm main (file ta đang chạy thực thi) kèm theo địa chỉ lưu trữ nó
- Constructor. Từ khóa self sẽ nhận giá trị chính là đối tượng đã gọi hàm init. Không có câu lệnh nào gọi hàm init. Thực tế hàm init tự động được gọi khi khởi tạo đối tượng. 
  - Khi dùng lớp SieuNhan khởi tạo đối tượng sieu_nhan_A, mặc định đã kêu đối tượng sieu_nhan_A gọi hàm init. 
  - Mặc định self được gán bằng đối tượng sieu_nhan_A
  - Các arg còn lại sẽ lần lượt được truyền vào bởi các tham số theo thứ tự
  - Mỗi khi có một đối tượng nào đó gọi một hàm thì luôn luôn tối thiểu sẽ có một argument được gửi vào hàm đó, chính là chính đối tượng đó, nếu hàm đó không có parameter nhận thì sẽ sinh lỗi, còn nếu dư argument (vì ta không lường trước được có một argument là chính đối tượng được ngầm gửi vào) thì vẫn sẽ có lỗi tràn argument.

2. Khai báo thuộc tính lớp trong lập trình hướng đối tượng với Python
- khi thay đổi giá trị một thuộc tính được khai báo trong lớp, ngoài constructor thông qua lớp thì thuộc tính ở toàn bộ đối tượng thuộc lớp đó sẽ được cập nhật lại giá trị mới được thay đổi.
- Cập nhật giá trị của thuộc tính (được khai báo trong class ngoài constructor) thông qua constructor
  - Thuộc tính so_thu_tu được thay đổi qua mỗi lần tạo đối tượng mới vì mỗi lần tạo đối tượng mới là ta lại gọi hàm constructor, do đó gián tiếp thay đổi giá trị so_thu_tu của lớp.
  - Ta gán giá trị này cho một thuộc tính của đối tượng đó ngay trong hàm constructor chứ  không để cho lớp giữ. Vì nếu đễ cho lớp giữ thì như bạn đã biết, nó sẽ thay đổi chứ không hề giữ nguyên sau các lần tạo đối tượng mới.
- Cập nhật giá trị thuộc tính thông qua object
  - Khi bạn thay đổi giá trị thuộc tính của một đối tượng, thì chỉ có đối tượng đó bị thay đổi, còn class vẫn như vậy. Và dĩ nhiên nếu như có nhiều đối tượng khác nó cũng vẫn sẽ không bị ảnh hưởng chung.
- khi khai báo thuộc tính của một đối tượng ở ngay trong class luôn thì nó cũng chỉ vẫn là thuộc tính, vì thế bạn vẫn có thể sử dụng nó ở trong các phương thức một cách bình thường như những thuộc tính được khởi tạo ngay trong hàm constructor

3. Các phương thức lớp trong lập trình hướng đối tượng với Python
- Những phương thức mà có mặc định parameter self gọi là regular method
- Ngoài ra còn có class method và static method
- Nếu regular method có argument đầu tiên tự động đưa vào là đối tượng đó và được nhận bởi parameter self thì ở class method, argument đầu tiên tự động đưa vào chính **lớp gọi phương thức đó** hoặc là **lớp của đối tượng gọi phương thức đó**
- Theo quy ước thì parameter nhận argument này sẽ là **cls**. Để Python biết được phương thức nào là class method thì thêm @classmethod ngay trên dòng khai báo hàm. Mặc định sẽ luôn có một argument được gửi vào đó chính là lớp gọi phương thức đó. Hoặc lớp của đối tượng gọi phương thức đó
- Tuy nhiên, ứng dụng chủ yếu của class method là để tạo đối tượng
- VD, muốn khởi tạo một siêu nhân nhưng một số siêu nhân có các thông tin không tường mình mà lại được lưu dưới dạng 1 list hay 1 chuỗi. Cần có 1 bước tiền xử lý trước khi ra được các thông tin của 1 siêu nhân nào đó mới tạo được 1 đối tượng
- Static method
  - Regular method được gửi vào arg là chính đối tượng gọi method và ta sử dụng parameter self để xử lý
  - Class method được gửi vào arg là chính class gọi phương thức và sử dụng parameter cls để xử lý
  - Static method không gửi gì, nó như một hàm bình thường
- Cách dùng
  - Nếu dựng 1 method cần sử dụng object thì dùng regular method
  - Cần dùng class thì dùng class method
  - TH còn lại - tức không dùng gì thì dùng static method
  
4. Tạo lớp kế thừa trong lập trình hướng đối tượng với Python
- super()
- Kế thừa thuộc tính
- Kế thừa constructor
- Kế thừa method


