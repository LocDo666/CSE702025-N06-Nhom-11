# CSE702025-N06-Nhom-11
 TÓM TẮT QUY TRÌNH XÂY DỰNG HỆ THỐNG QUẢN LÝ KHO VẬT TƯ
✅ 1. Xác định chức năng hệ thống
Hệ thống cần đảm nhiệm các chức năng chính:

Thêm vật tư

Sửa thông tin vật tư

Xóa vật tư

Tìm kiếm vật tư

Hiển thị danh sách vật tư trong bảng

✅ 2. Chọn công nghệ
Ngôn ngữ lập trình: Python

Loại ứng dụng: Ứng dụng Desktop (giao diện Tkinter)

IDE: Visual Studio Code (VS Code)

Cơ sở dữ liệu: MySQL

Thư viện kết nối cơ sở dữ liệu: mysql-connector-python

✅ 3. Thiết kế cơ sở dữ liệu
Tên cơ sở dữ liệu: kho_vattu

Tên bảng chính: vat_tu

Các trường trong bảng:

Mã vật tư (maVT) – Khóa chính

Tên vật tư (tenVT)

Số lượng (soLuong)

Đơn giá (donGia)

Nhà cung cấp (nhaCungCap)

✅ 4. Tạo project trong VS Code
Cấu trúc thư mục gợi ý:

Thư mục assets chứa hình ảnh, logo nếu có

Thư mục db chứa tệp kết nối cơ sở dữ liệu

Thư mục models chứa các hàm thao tác dữ liệu (thêm, xóa, sửa, tìm kiếm)

Thư mục ui chứa các tệp thiết kế giao diện bằng Tkinter

Tệp main.py để chạy chương trình

Tệp requirements.txt để khai báo thư viện cần cài đặt

✅ 5. Kết nối Python với MySQL
Cài đặt thư viện kết nối MySQL

Tạo một tệp riêng để mở kết nối với cơ sở dữ liệu

Viết các hàm để:

Lấy toàn bộ dữ liệu vật tư

Thêm vật tư mới

Cập nhật thông tin vật tư

Xóa vật tư

Tìm kiếm vật tư

✅ 6. Thiết kế giao diện bằng Tkinter
Giao diện gồm:

Bảng hiển thị danh sách vật tư (dùng Treeview)

Các ô nhập liệu: mã vật tư, tên, số lượng, đơn giá, nhà cung cấp

Các nút chức năng: Thêm – Sửa – Xóa – Làm mới

✅ 7. Kết nối giao diện với dữ liệu
Khi mở chương trình: tự động hiển thị toàn bộ dữ liệu vật tư

Khi chọn dòng trong bảng: dữ liệu hiển thị lên ô nhập để chỉnh sửa

Các nút chức năng tương tác với cơ sở dữ liệu (thêm mới, cập nhật, xóa)

✅ 8. Kiểm thử và hoàn thiện hệ thống
Kiểm tra tính chính xác và tính hợp lệ của dữ liệu đầu vào

Kiểm thử các chức năng thêm – sửa – xóa – tìm kiếm

✅ Phân công công việc nhóm 
Người 1: Thiết kế cơ sở dữ liệu

Người 2: Thiết kế giao diện

Người 3: Kết nối và xử lý logic chương trình

Người 4: Kiểm thử và viết báo cáo tổng kết
  
