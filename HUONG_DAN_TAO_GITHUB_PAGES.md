# HƯỚNG DẪN ĐƯA BÁO CÁO NHÂN LỰC LÊN TÊN MIỀN GITHUB.IO (MIỄN PHÍ 100%)

Sử dụng **GitHub Pages (`github.io`)** là **LỰA CHỌN TỐI ƯU NHẤT** cho ứng dụng báo cáo này vì:
- 🚀 **100% Sạch sẽ**: Tuyệt đối **KHÔNG có bất kỳ dòng chữ cảnh báo (Warning)** nào của Google.
- ⚡ **Tốc độ cực nhanh**: Tải trang tức thì qua mạng CDN toàn cầu của GitHub.
- 🔒 **Bảo mật & Miễn phí trọn đời**: Tự động có chứng chỉ bảo mật HTTPS (`https://`).
- 📱 **Hỗ trợ điện thoại hoàn hảo**: Không bị đóng khung trong iframe, in PDF chuẩn tăm tắp, thêm vào màn hình chính iPhone (Add to Home Screen) dùng mượt như App thật.

---

## CÁCH 1: LÀM TRÊN TRÌNH DUYỆT WEB (DỄ NHẤT - CHỈ MẤT 1 PHÚT)

### Bước 1: Tạo Repository trên GitHub
1. Truy cập [github.com](https://github.com) và đăng nhập (nếu chưa có tài khoản, anh đăng ký miễn phí chỉ mất 30 giây).
2. Bấm vào biểu tượng dấu **`+`** ở góc trên bên phải $\rightarrow$ chọn **New repository**.
3. Điền thông tin:
   - **Repository name**: ví dụ đặt là `baocao-nhanluc` (hoặc `cienco510`).
   - Chọn chế độ: **Public** (để dùng được tính năng GitHub Pages miễn phí).
   - Tích chọn ô: **Add a README file**.
4. Bấm nút màu xanh **Create repository**.

---

### Bước 2: Tải file `index.html` lên
1. Trong trang repository vừa tạo, bấm nút **Add file** $\rightarrow$ chọn **Upload files**.
2. Kéo thả file **`index.html`** từ máy tính của anh (nằm ở thư mục `/Users/hanario/Documents/quyen/index.html`) vào khung tải lên của GitHub.
3. Cuộn xuống dưới cùng và bấm nút màu xanh **Commit changes**.

---

### Bước 3: Kích hoạt GitHub Pages
1. Ở thanh menu trên cùng của repository, bấm vào tab **Settings** (Cài đặt).
2. Ở cột menu bên trái, tìm và bấm vào mục **Pages** (trong phần *Code and automation*).
3. Tại mục **Build and deployment**:
   - **Source**: Chọn **Deploy from a branch**.
   - **Branch**: Chọn nhánh `main` (hoặc `master`), thư mục giữ nguyên là `/ (root)`.
   - Bấm nút **Save**.
4. Đợi khoảng **30 - 60 giây**, tải lại trang Settings -> Pages:
   GitHub sẽ hiện thông báo màu xanh lá cây kèm đường link công khai của anh, có dạng:
   👉 **`https://<tên-tài-khoản-của-anh>.github.io/baocao-nhanluc/`**

*(Nếu anh muốn đường link ngắn gọn nhất dạng `https://<tên-tài-khoản>.github.io/`, chỉ cần đặt tên Repository lúc tạo ở Bước 1 đúng bằng `<tên-tài-khoản>.github.io`)*.

---

## CÁCH 2: DÙNG DÒNG LỆNH GIT TRÊN MÁY MAC (NẾU ANH QUEN DÙNG TERMINAL)

Mở Terminal trên máy Mac và chạy các lệnh sau:

```bash
cd /Users/hanario/Documents/quyen

# Khởi tạo git
git init
git add index.html
git commit -m "Khoi tao web app bao cao nhan luc CIENCO 510"

# Đổi nhánh sang main
git branch -M main

# Liên kết với repo GitHub (thay <username> và <repo> bằng tài khoản của anh)
git remote add origin https://github.com/<username>/<repo>.git

# Đẩy mã nguồn lên
git push -u origin main
```
Sau đó vào **Settings** $\rightarrow$ **Pages** trên GitHub và bật nhánh `main` như Bước 3 ở trên.

---

## 📱 CÁCH SỬ DỤNG TRÊN IPHONE / ANDROID:
1. Gửi đường link `https://<username>.github.io/baocao-nhanluc/` vào nhóm Zalo / Telegram công trường.
2. Khi mở trên iPhone bằng Safari:
   - Giao diện tự động phân bổ dọc chuẩn Smartphone.
   - Bấm **Chia sẻ** $\rightarrow$ **Thêm vào MH chính (Add to Home Screen)** để tạo icon App Báo Cáo trên màn hình iPhone.
   - Khi bấm **In / Xuất PDF (A4)** hoặc **In hình ảnh**: Xuất ngay file PDF/ảnh chuẩn A4 Landscape sạch 100%, sắc nét, không có bất kỳ dòng chữ lạ nào!
