# HƯỚNG DẪN SỬ DỤNG BỘ TEMPLATE BÁO CÁO NHÂN LỰC HÀNG NGÀY TẠI CÔNG TRƯỜNG

Bộ template được thiết kế chuẩn theo mẫu báo cáo hiện trường, phục vụ việc nhập liệu linh hoạt, tự động tính tổng và xuất bản in/PDF chất lượng cao khổ A4 ngang.

Thư mục lưu trữ: `/Users/hanario/Documents/quyen`

---

## 📁 Cấu Trúc Thư Mục

```text
hanario/Documents/quyen/
├── index.html                   # Giao diện Web tương tác, nhập trực tiếp và in/xuất PDF
├── Bao_Cao_Nhan_Luc_Hang_Ngay.xlsx # File mẫu Excel chuẩn có công thức tính tổng tự động
├── data_mau.json                # Tệp dữ liệu mẫu JSON
├── generate_report.py           # Script tự động sinh file Excel từ file JSON
├── create_excel_template.py     # Script tạo file template Excel ban đầu
├── assets/                      # Thư mục chứa hình ảnh
│   ├── banner_cienco510.png     # Banner logo góc phải trên
│   └── signature_sample.png     # Chữ ký mẫu Chỉ huy trưởng
└── HUONG_DAN_SU_DUNG.md         # Bản hướng dẫn này
```

---

## 🚀 Cách 1: Sử dụng Giao diện Web Tương tác (`index.html`)

Đây là cách **thuận tiện, nhanh chóng và trực quan nhất**. Bạn không cần cài đặt phần mềm nào khác.

### 1. Mở giao diện
- Nhấp đúp chuột vào tệp `index.html` để mở trong trình duyệt (Google Chrome, Safari, Microsoft Edge, Cốc Cốc,...).

### 2. Chỉnh sửa nội dung tùy ý (WYSIWYG)
- **Thông tin chung**: Nhấp chuột trực tiếp vào các mục màu đỏ: *Tên dự án, Gói thầu, Nhà thầu, Ngày báo cáo* để sửa.
- **Thời tiết**: Tích chọn trực tiếp vào các ô `☀️ Nắng`, `🌧️ Mưa`, `☁️ Âm u` hoặc nhập vào mục `Khác`.
- **Thêm / Xóa dòng**:
  - Bấm nút `+ Thêm dòng` ở góc phải tiêu đề mỗi phần (Phần 1, 2, 4) để thêm công việc hoặc tổ đội mới.
  - Bấm biểu tượng dấu `×` màu xám ở cuối mỗi hàng để xóa dòng đó.
- **Tự động tính toán**: 
  - Khi bạn thay đổi số lượng nhân lực ở các bảng, dòng **TỔNG CỘNG** và chỉ số tại mục **3. Đánh giá tình hình nhân lực** sẽ **tự động cập nhật ngay lập tức**.
  - Tiêu đề mục **4. KẾ HOẠCH NHÂN LỰC NGÀY MAI (ngày/tháng/năm)** sẽ tự động tính ngày tiếp theo dựa trên ngày báo cáo bạn nhập.
- **Đổi Logo / Banner & Chữ ký**:
  - Rê chuột vào góc phải vùng Banner hoặc vùng Chữ ký sẽ xuất hiện nút `Đổi ảnh banner` / `Đổi chữ ký`. Bấm vào để chọn ảnh logo hoặc chữ ký từ máy tính của bạn.

### 3. Tự động lưu & Dùng lại "Báo cáo trước"
- **Tự động lưu mốc xuất file**: Mỗi khi bạn bấm **"In / Xuất PDF (A4)"** hoặc **"In hình ảnh"**, hệ thống sẽ tự động lưu lại toàn bộ nội dung của báo cáo đó làm mốc **"Báo cáo trước"** (lần xuất file gần nhất).
- **Dùng lại Báo cáo trước**: Khi cần làm báo cáo mới cho ca/ngày tiếp theo, chỉ cần bấm nút **`Báo cáo trước`** trên thanh công cụ:
  - Toàn bộ danh sách tổ đội, nội dung công việc, thiết bị và số lượng từ lần xuất file gần nhất sẽ được nạp lại ngay lập tức.
  - **Ngày báo cáo** sẽ tự động được cập nhật sang ngày hôm nay (`today`), đồng thời kế hoạch ngày mai cũng được tự động đồng bộ theo (`today + 1`).
- **Mẫu ban đầu**: Bấm nút `Mẫu ban đầu` nếu muốn khôi phục giao diện về trạng thái bảng mẫu mặc định gốc.

### 4. Xuất file PDF hoặc In ra giấy
- Bấm nút **"In / Xuất PDF (A4)"** trên thanh công cụ (hoặc phím tắt `Ctrl + P` trên Windows / `Cmd + P` trên Mac).
- Cài đặt in trong hộp thoại trình duyệt:
  - **Máy in (Destination)**: Chọn *Save as PDF (Lưu dưới dạng PDF)* hoặc chọn máy in văn phòng.
  - **Bố cục (Layout)**: Chọn **Landscape (Khổ ngang)**.
  - **Khổ giấy (Paper size)**: **A4**.
  - **Tỷ lệ (Scale)**: Mặc định (Default) hoặc Fit to printable area (100%).
  - **Tùy chọn (Options)**: Tích chọn **Background graphics (Đồ họa nền)** để giữ nguyên màu sắc thanh tiêu đề và bảng biểu.

---

## 📊 Cách 2: Sử dụng Bảng tính Excel (`Bao_Cao_Nhan_Luc_Hang_Ngay.xlsx`)

Dành cho người dùng quen làm việc trên bảng tính Excel.

1. Mở file `Bao_Cao_Nhan_Luc_Hang_Ngay.xlsx` bằng Microsoft Excel, WPS Office, Apple Numbers hoặc tải lên Google Sheets.
2. Nhập các số liệu vào bảng:
   - Các ô số lượng hiển thị chữ đỏ đậm nổi bật.
   - Các ô **TỔNG CỘNG** đã được gắn sẵn công thức `=SUM(...)`.
   - Mục **3. Đánh giá tình hình nhân lực** đã tự động lấy số tổng từ bảng 1 (`=E16 & " người."`).
3. Vùng in đã được định dạng sẵn:
   - Khổ giấy: **A4**.
   - Hướng trang: **Ngang (Landscape)**.
   - Thiết lập tự động: **Fit to 1 page wide by 1 page tall** (Vừa khít 1 trang A4 ngang, không bao giờ bị nhảy trang).

---

## 🤖 Cách 3: Sử dụng Script Python Tự động hóa (`generate_report.py`)

Dành cho lập trình viên hoặc khi muốn kết nối hệ thống xuất báo cáo tự động:

```bash
cd /Users/hanario/Documents/quyen

# Chạy với dữ liệu mẫu mặc định:
python3 generate_report.py

# Hoặc truyền file JSON tùy biến và tên file Excel đầu ra:
python3 generate_report.py du_lieu_ngay_16.json Bao_Cao_16_07.xlsx
```

---

*Chúc bạn hoàn thành tốt các báo cáo hiện trường nhanh chóng và chính xác!*

---

## 📲 Cách 4: Gửi Báo Cáo Trực Tiếp Qua Telegram (`send_to_telegram.py`)

Hệ thống đã tích hợp sẵn script gửi file báo cáo (PDF, Excel, Ảnh) đến nhóm Telegram qua Bot:

```bash
cd /Users/hanario/Documents/quyen

# Gửi file PDF 99 người:
python3 send_to_telegram.py Bao_Cao_Nhan_Luc_99_Nguoi.pdf "Báo cáo nhân lực ngày 18/07"

# Gửi file Excel:
python3 send_to_telegram.py Bao_Cao_Nhan_Luc_99_Nguoi.xlsx "File Excel số liệu nhân lực"

# Gửi ảnh xem trước:
python3 send_to_telegram.py assets/preview_99_nguoi.png "Ảnh chụp báo cáo"
```

---

## 🎨 Cách 5: Sử Dụng Trình Thiết Kế Kéo Thả & Tùy Biến Cấu Trúc (`designer.html`)

Dành cho khi bạn muốn **thay đổi toàn diện cấu trúc**, di chuyển các khối, thêm khung viền, chỉnh font chữ, hoặc chèn thêm bảng/hình ảnh mới:

### 1. Mở công cụ
- Nhấp đúp chuột vào file [`designer.html`](./designer.html) trên trình duyệt.

### 2. Các thao tác chính
- **Kéo di chuyển (Drag & Drop)**: Bấm giữ chuột vào bất kỳ khối nào (Tiêu đề, Bảng thống kê, Banner, Đánh giá, Chữ ký...) để di chuyển đến vị trí bất kỳ trên trang A4 ngang.
- **Co giãn kích thước (Resize)**: Nhấp chuột vào một khối để hiện 8 điểm neo màu xanh ở các góc và cạnh, kéo các điểm này để thay đổi chiều rộng, chiều cao.
- **Tùy biến Viền (Borders)**:
  - Kiểu viền: Nét liền (Solid), Nét đứt (Dashed), Nét chấm (Dotted), Nét đôi (Double), Không viền.
  - Độ dày viền: 1px, 1.5px, 2px, 3px, 4px...
  - Màu viền: Bấm vào ô chọn màu để chọn màu viền bất kỳ.
  - Bo góc (Border Radius): 0px (vuông), 4px, 8px, 12px, 20px (tròn).
- **Màu nền (Background Fill)**:
  - Chọn không nền (Trong suốt), nền Trắng, nền Xanh nhạt `#EBF1F8`, Xám nhạt, hoặc màu tự chọn.
- **Thao tác Chữ (Typography)**:
  - Nhấp đúp vào bất kỳ đoạn văn hoặc ô bảng nào để sửa trực tiếp.
  - Đổi Font chữ (*Roboto, Be Vietnam Pro, Arial, Times New Roman*).
  - Đổi cỡ chữ (11px, 12px, 13px, 14px, 16px, 18px, 22px, 26px...).
  - Đổi màu chữ, In đậm (B), In nghiêng (I), Gạch chân (U), Căn lề Trái/Giữa/Phải.
- **Chèn thêm phần tử mới**:
  - `+ Ô chữ`: Chèn thêm một khối văn bản mới.
  - `+ Khung viền`: Tạo khung nhóm mới để đóng khung phân khu.
  - `+ Đường kẻ`: Thêm đường phân cách ngang/dọc.
  - `+ Bảng mới`: Chèn một bảng số liệu tùy chỉnh.
  - `+ Ảnh / Logo`: Tải thêm hình ảnh hoặc logo từ máy tính.
- **Thứ tự lớp & Căn chỉnh**:
  - `Lên trước` / `Về sau` để sắp xếp khối nằm đè lên nhau.
  - `Căn giữa`: Canh khối nằm ngay giữa khổ giấy.
  - `Xoá khối`: Loại bỏ khối không dùng đến.

### 3. Lưu, Nạp và In / Xuất PDF
- **Lưu Layout (.json)**: Tải file cấu hình vị trí và kiểu dáng về máy.
- **Nạp Layout**: Chọn file `.json` đã lưu để khôi phục cấu trúc.
- **In / Xuất PDF (A4)**: Tự động ẩn sạch thanh công cụ, các điểm kéo co giãn và lưới định vị; in chuẩn khổ A4 ngang sắc nét.
