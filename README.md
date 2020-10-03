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
