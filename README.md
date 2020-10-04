# python_oop

1. Một số khái niệm
- Class: là một kiểu dữ liệu người dùng tự định nghĩa,tập hợp nhiều thuộc tính đặc trưng cho mọi đối tượng được tạo ra từ lớp đó. Các thuộc tính là các biến thành viên hoặc phương thức
- Object: là một thể hiện cụ thể của CTDL được định nghĩa trong lớp. Mỗi object bao gồm cả biến thành viên và phương thức
- Data member: là biến được định nghĩa trong class hoặc object
- Method: là hàm được định nghĩa trong class nhằm thực hiện 1 công việc cụ thể
- Inheritace: là một tính chất của các ngôn ngữ OOP cho phép các class kế thừa các đặc trưng của lớp được kế thừa
2. Định nghĩa class
- Cú pháp class classname:
- Dòng đầu sử dụng string để mô tả ngắn gọn về class (không bắt buộc) 
  + Truy cập chuỗi này thông qua classname.__doc__
- Trong phần thân khai báo attribute (thuộc tính), method (phương thức) và constructor (phương thức khởi tạo)

3. Attribute
- Attribute là thành viên của lớp
- VD hình chữ nhật có 2 thuộc tính là width và height
4. Method
- Method là 1 hàm thông thường, nhưng là 1 hàm của class
- Để sử dụng Method cần gọi thông qua Object
- Tham số đầu tiên của Method luôn là self
5. Constructor
- Là phương thức khởi tạo. Là một method đặc biệt của class, nó luôn có tên là __init__
- Tham số đầu tiên của constructor luôn là self
- Constructor được dùng để tạo ra một object
- Constructor gán giá trị từ tham số vào các attribute của object sẽ được tạo ra
- Có thể định nghĩa nhiều nhất 1 constructor trong class
- Nếu class không được định nghĩa constructor, python mặc định coi rằng nó kế thừa từ constructor của lớp cha
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
- Mỗi biến của lớp có 1 địa chỉ
13. Liệt kê danh sách các thành viên 

14. Hủy đối tượng

