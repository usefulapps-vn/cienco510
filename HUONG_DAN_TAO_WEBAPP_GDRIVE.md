# HƯỚNG DẪN TẠO WEB APP BÁO CÁO NHÂN LỰC TRÊN GOOGLE DRIVE (MIỄN PHÍ 100%)

Với Google Apps Script trên Google Drive, anh có thể xuất bản ứng dụng báo cáo này thành một đường link Web App công khai:
- Mọi kỹ sư, chỉ huy trưởng đều có thể truy cập từ điện thoại di động (iPhone, Android) hoặc máy tính.
- Responsive dễ nhìn, dễ nhập liệu trên điện thoại.
- Khi bấm **In / Xuất PDF** hoặc **In hình ảnh**, định dạng giữ nguyên 100% chuẩn A4 ngang CIENCO 510.

---

## CÁC BƯỚC THỰC HIỆN (CHỈ MẤT 2 PHÚT):

### BƯỚC 1: Tạo dự án Apps Script trên Google Drive
1. Mở trình duyệt web, vào [script.google.com](https://script.google.com) (đăng nhập tài khoản Google).
2. Bấm nút **+ Dự án mới** (New Project) ở góc trên bên trái.
3. Đặt tên dự án (ví dụ: `Bao Cao Nhan Luc CIENCO 510`).

### BƯỚC 2: Dán mã nguồn `Code.gs`
1. Ở khung code có sẵn file `Mã.gs` (hoặc `Code.gs`), xóa hết nội dung cũ và dán đoạn sau vào:

```javascript
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Báo Cáo Nhân Lực Hàng Ngày - CIENCO 510')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
```

### BƯỚC 3: Tạo file `Index.html`
1. Tại cột bên trái (mục Tệp / Files), bấm dấu **+** và chọn **HTML**.
2. Đặt tên file là `Index` (hệ thống sẽ tự hiểu là `Index.html`).
3. Mở file [index.html](file:///Users/hanario/Documents/quyen/index.html) trên máy của anh:
   - Chọn tất cả (`Ctrl + A` hoặc `Cmd + A`).
   - Sao chép (`Ctrl + C` hoặc `Cmd + C`).
4. Dán toàn bộ nội dung đó vào file `Index.html` trên Google Apps Script.
5. Bấm biểu tượng **Lưu (Save / Ctrl + S)**.

### BƯỚC 4: Triển khai thành Web App (Deploy)
1. Ở góc trên bên phải, bấm nút **Triển khai (Deploy)** -> Chọn **Tùy chọn triển khai mới (New deployment)**.
2. Tại mục bánh răng (Chọn loại / Select type), chọn **Ứng dụng web (Web app)**.
3. Điền thông tin:
   - **Mô tả**: Báo cáo nhân lực hàng ngày
   - **Thực thi dưới tên (Execute as)**: *Tôi (tài khoản của anh)*
   - **Ai có quyền truy cập (Who has access)**: *Bất kỳ ai (Anyone)* - để gửi link cho anh em công trường mở được ngay mà không bắt đăng nhập phức tạp.
4. Bấm **Triển khai (Deploy)**.
5. Google sẽ cấp cho anh một đường link dạng:
   `https://script.google.com/macros/s/.../exec`

> [!TIP]
> **Khi cập nhật code mới vào Google Apps Script:**
> Sau khi dán code mới vào `Index.html` và bấm Lưu (Ctrl + S):
> 1. Bấm **Triển khai (Deploy)** -> Chọn **Quản lý phiên triển khai (Manage deployments)**.
> 2. Bấm vào biểu tượng **Chỉnh sửa (Cây bút chì ✏️)** ở góc trên bên phải.
> 3. Tại mục **Phiên bản (Version)**, bấm chọn **Phiên bản mới (New version)**.
> 4. Bấm **Triển khai (Deploy)**. Đường link Web App cũ sẽ tự động nhận giao diện và tính năng mới nhất!

---

## 📸 TÍNH NĂNG "IN HÌNH ẢNH" & "XUẤT PDF" ĐÃ ĐƯỢC NÂNG CẤP HOÀN TOÀN ĐỘC LẬP:
- **100% Tự động & Không lỗi thư viện**: Toàn bộ thư viện đồ họa `html2canvas` đã được tích hợp nhúng thẳng vào file `Index.html`, không phụ thuộc đường dẫn ngoài, chạy mượt mà 100% trên máy chủ Google Apps Script.
- **Hỗ trợ iPhone / Safari / Web App**: Khi bấm **"📸 In hình ảnh"**, một cửa sổ xem trước sẽ hiện ra ngay lập tức.
  - Trên điện thoại: Chỉ cần chạm và **giữ im vào ảnh**, sau đó chọn **"Lưu hình ảnh" (Save to Photos)** hoặc bấm **"Chia sẻ"** gửi thẳng vào nhóm Zalo / Telegram công trường!
  - Trên máy tính: Ảnh `.png` sắc nét 2048 x 1364 px sẽ tự động tải về thư mục Downloads.
- **In / Xuất PDF (A4) Chuẩn Tuyệt Đối**:
  - Tự động scale 0.92 và căn lề an toàn 18px trên mọi thiết bị.
  - Tự động khóa định dạng màu sắc `-webkit-print-color-adjust: exact`, chống mất nền xanh và chống lệch góc, mất viền khi in từ Google Chrome, Cốc Cốc, Safari hay Edge.

---

## 📱 TÍNH NĂNG CHUYỂN ĐỔI CHẾ ĐỘ XEM (DESKTOP / SMARTPHONE):
- **Tự động nhận diện**: Khi mở trên điện thoại (màn hình $\le$ 768px), hệ thống sẽ tự động bật chế độ **Smartphone** hiển thị các mục xếp dọc theo đúng thứ tự 1 -> 2 -> 3 -> 4 -> 5, vừa khít màn hình không bị tràn ngang.
- **Nút Toggle trên thanh công cụ**:
  - Bấm `💻 Desktop`: Chuyển về xem toàn bộ khổ giấy A4 ngang nguyên bản.
  - Bấm `📱 Smartphone`: Chuyển về dạng danh sách dọc tiện lợi cho điện thoại.
- **Bảo lưu tuyệt đối khi In / Xuất ảnh**:
  - Dù đang ở chế độ xem Smartphone hay Desktop, khi bấm **In / Xuất PDF (A4)** hoặc **In hình ảnh**, hệ thống luôn tự động xuất chuẩn **1 trang A4 ngang CIENCO 510 (1024 x 682 px)** với lề cân đối chuẩn chỉ!

---

## 📱 CÁCH SỬ DỤNG TRÊN ĐIỆN THOẠI:
- Gửi link Web App qua nhóm Zalo / Telegram.
- Trên iPhone / Android, mở link bằng Safari hoặc Chrome.
- **Mẹo hay**: Bấm nút chia sẻ trên Safari -> Chọn **"Thêm vào Màn hình chính" (Add to Home Screen)** để biến trang web thành một ứng dụng tiện lợi mở nhanh như app cài đặt!
