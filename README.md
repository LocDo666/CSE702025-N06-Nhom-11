# CSE702025-N06-Nhom-11
🧭 TÓM TẮT QUY TRÌNH XÂY HỆ THỐNG QUẢN LÝ KHO VẬT TƯ Ô TÔ

  ✅ 1. Xác định chức năng hệ thống
    Quản lý thông tin vật tư (thêm, sửa, xóa, tìm kiếm)
    Hiển thị danh sách vật tư    
    (Tuỳ chọn) Thống kê, xuất Excel...
    
  ✅ 2. Chọn công nghệ
    Ngôn ngữ: Java
    Loại ứng dụng: Desktop App (giao diện Swing)  
    IDE: Apache NetBeans
    Cơ sở dữ liệu: MySQL    
    Thư viện kết nối: JDBC (MySQL Connector)
    
  ✅ 3. Thiết kế cơ sở dữ liệu
  Tạo database kho_vattu  
  Tạo bảng vat_tu với các trường: 
  maVT (PK), tenVT, soLuong, donGia, nhaCungCap
  
  ✅ 4. Tạo project Java
  Tạo project Java trong NetBeans 
  Cấu trúc thư mục:
  bash
  Copy
  Edit
  /model      → class VatTu.java
  /dao        → DBConnect.java, VatTuDAO.java
  /view       → Giao diện Swing (form chính)
  
  ✅ 5. Kết nối Java ↔ MySQL
  Thêm thư viện mysql-connector-java vào project  
  Tạo lớp DBConnect để mở kết nối database  
  Viết DAO để:  
  Lấy dữ liệu (getAllVatTu) 
  Thêm vật tư (insertVatTu) 
  (Có thể thêm update, delete, search...)
  
  ✅ 6. Thiết kế giao diện bằng Swing
  Form chính gồm:  
  Bảng hiển thị danh sách vật tư  
  Các ô nhập thông tin: mã, tên, số lượng, đơn giá, nhà cung cấp 
  Các nút: Thêm, Sửa, Xóa, Làm mới
  
  ✅ 7. Kết nối logic giao diện với dữ liệu
  Khi ấn nút “Thêm” → gọi insertVatTu(...)  
  Khi mở chương trình → gọi getAllVatTu() → đổ vào JTable  
  Khi chọn hàng → hiển thị thông tin lên ô nhập  
  Khi “Xóa”, “Sửa” → cập nhật hoặc xóa dữ liệu trong database
  
  ✅ 8. Test, hoàn thiện và báo cáo
  Kiểm thử dữ liệu, kiểm tra lỗi nhập 
  Bổ sung giao diện đẹp hơn (tuỳ ý)  
  Làm báo cáo: UML, ảnh giao diện, mô tả chức năng, mã nguồn
  
  📌 Gợi ý trình bày báo cáo
  Mục tiêu hệ thống  
  Công nghệ sử dụng  
  Thiết kế CSDL (ERD hoặc bảng thực tế)  
  Mô hình lớp (class diagram)  
  Ảnh giao diện (form Swing)  
  Một số đoạn code tiêu biểu (DAO, kết nối DB)  
  
  Nhận xét – Đánh giá  
  Bạn có thể mang bản tóm tắt này đi thảo luận nhóm, chia task theo phần: 
  
  Người 1: thiết kế CSDL + tạo DAO 
  
  Người 2: làm giao diện 
  
  Người 3: kết nối và xử lý sự kiện  
  
  Người 4: viết báo cáo, test
