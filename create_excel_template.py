import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.drawing.image import Image

def create_template():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Báo Cáo Nhân Lực"

    # Color definitions
    NAVY = "0B3064"
    NAVY_LIGHT = "EBF1F8"
    RED = "B92521"
    BORDER_COLOR = "9FB8D4"
    WHITE = "FFFFFF"
    GRAY_TEXT = "555555"

    font_title = Font(name="Arial", size=15, bold=True, color=NAVY)
    font_sub_title = Font(name="Arial", size=11, bold=True, color=NAVY)
    font_meta_label = Font(name="Arial", size=9.5, bold=True, color=NAVY)
    font_meta_val = Font(name="Arial", size=9.5, bold=True, color=RED)
    font_sec_hdr = Font(name="Arial", size=10, bold=True, color=WHITE)
    font_tbl_hdr = Font(name="Arial", size=9, bold=True, color=NAVY)
    font_tbl_data = Font(name="Arial", size=9.5, color="000000")
    font_tbl_num = Font(name="Arial", size=10, bold=True, color=RED)
    font_total_lbl = Font(name="Arial", size=10, bold=True, color=NAVY)
    font_total_num = Font(name="Arial", size=12, bold=True, color=RED)

    fill_sec_hdr = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
    fill_tbl_hdr = PatternFill(start_color=NAVY_LIGHT, end_color=NAVY_LIGHT, fill_type="solid")
    fill_total = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    thin_border_side = Side(style="thin", color=BORDER_COLOR)
    medium_navy_side = Side(style="medium", color=NAVY)
    box_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    # Column widths
    ws.column_dimensions['A'].width = 5.5   # STT
    ws.column_dimensions['B'].width = 17    # Team name part 1
    ws.column_dimensions['C'].width = 8     # Team 1 count
    ws.column_dimensions['D'].width = 17    # Team name part 2
    ws.column_dimensions['E'].width = 9     # Team 2 count / Sec 1 count
    ws.column_dimensions['F'].width = 2.5   # Spacer
    ws.column_dimensions['G'].width = 12    # Khu vực
    ws.column_dimensions['H'].width = 33    # Nội dung công việc
    ws.column_dimensions['I'].width = 15    # Số lượng nhân công

    # Row Heights
    ws.row_dimensions[1].height = 22
    ws.row_dimensions[2].height = 18
    ws.row_dimensions[3].height = 18
    ws.row_dimensions[4].height = 18
    ws.row_dimensions[5].height = 18
    ws.row_dimensions[6].height = 18
    ws.row_dimensions[7].height = 6 # Spacer
    ws.row_dimensions[8].height = 22 # Section headers
    ws.row_dimensions[9].height = 20 # Table headers

    # HEADER LEFT
    ws.merge_cells('A1:E1')
    ws['A1'] = "BÁO CÁO NHÂN LỰC HÀNG NGÀY"
    ws['A1'].font = font_title
    ws['A1'].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells('A2:E2')
    ws['A2'] = "TẠI CÔNG TRƯỜNG"
    ws['A2'].font = font_sub_title
    ws['A2'].alignment = Alignment(horizontal="center", vertical="center")

    # Project metadata
    ws['A3'] = "Dự án:"
    ws['A3'].font = font_meta_label
    ws.merge_cells('B3:E3')
    ws['B3'] = "Phát triển tích hợp thích ứng - tỉnh Bình Định"
    ws['B3'].font = font_meta_val

    ws['A4'] = "Gói thầu:"
    ws['A4'].font = font_meta_label
    ws.merge_cells('B4:E4')
    ws['B4'] = "BD-CW01: Đoạn đường từ QL 19C kết nối cảng Quy Nhơn (Km0-Km1+159.97)"
    ws['B4'].font = font_meta_val

    ws['A5'] = "Nhà thầu:"
    ws['A5'].font = font_meta_label
    ws.merge_cells('B5:C5')
    ws['B5'] = "Công ty Cổ phần XDCT 510"
    ws['B5'].font = font_meta_val

    ws['D5'] = "Ngày báo cáo:"
    ws['D5'].font = font_meta_label
    ws['D5'].alignment = Alignment(horizontal="right")
    ws['E5'] = "15/07/2026"
    ws['E5'].font = font_meta_val
    ws['E5'].alignment = Alignment(horizontal="center")

    ws['A6'] = "Thời tiết:"
    ws['A6'].font = font_meta_label
    ws.merge_cells('B6:E6')
    ws['B6'] = " [x] Nắng    [ ] Mưa    [ ] Âm u    Khác: ................."
    ws['B6'].font = Font(name="Arial", size=9, bold=False, color="1C2430")

    # HEADER RIGHT: Banner image
    banner_path = "/Users/hanario/Documents/quyen/assets/banner_cienco510.png"
    if os.path.exists(banner_path):
        img = Image(banner_path)
        img.width = 390
        img.height = 110
        ws.add_image(img, 'G1')

    # Border between header and body
    for col in range(1, 10):
        cell = ws.cell(row=7, column=col)
        cell.border = Border(bottom=thin_border_side)

    # -------------------------------------------------------------
    # SECTION 1: 1. THỐNG KÊ NHÂN LỰC (Rows 8 to 16)
    # -------------------------------------------------------------
    ws.merge_cells('A8:E8')
    ws['A8'] = "1. THỐNG KÊ NHÂN LỰC"
    ws['A8'].font = font_sec_hdr
    ws['A8'].fill = fill_sec_hdr
    ws['A8'].alignment = Alignment(horizontal="left", vertical="center", indent=1)

    # Headers for Table 1
    ws['A9'] = "STT"
    ws['A9'].font = font_tbl_hdr
    ws['A9'].fill = fill_tbl_hdr
    ws['A9'].alignment = Alignment(horizontal="center", vertical="center")
    ws['A9'].border = box_border

    ws.merge_cells('B9:D9')
    ws['B9'] = "BỘ PHẬN / TỔ ĐỘI"
    ws['B9'].font = font_tbl_hdr
    ws['B9'].fill = fill_tbl_hdr
    ws['B9'].alignment = Alignment(horizontal="center", vertical="center")
    for col in ['B', 'C', 'D']:
        ws[f'{col}9'].border = box_border

    ws['E9'] = "SỐ LƯỢNG (NGƯỜI)"
    ws['E9'].font = font_tbl_hdr
    ws['E9'].fill = fill_tbl_hdr
    ws['E9'].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws['E9'].border = box_border

    # Data rows for Table 1
    sec1_data = [
        ("Ban chỉ huy công trường", 2),
        ("Đội trưởng 22", 1),
        ("Công nhân đội 22", 15),
        ("Cơ giới", 4),
        ("Công ty Hà Thành", 8),
        ("Công ty Tấn Thành", 7),
    ]

    for idx, (bp, sl) in enumerate(sec1_data, start=1):
        r = 9 + idx
        ws.row_dimensions[r].height = 19
        ws[f'A{r}'] = idx
        ws[f'A{r}'].alignment = Alignment(horizontal="center", vertical="center")
        ws[f'A{r}'].font = font_tbl_data
        ws[f'A{r}'].border = box_border

        ws.merge_cells(f'B{r}:D{r}')
        ws[f'B{r}'] = bp
        ws[f'B{r}'].font = font_tbl_data
        ws[f'B{r}'].alignment = Alignment(horizontal="left", vertical="center", indent=1)
        for col in ['B', 'C', 'D']:
            ws[f'{col}{r}'].border = box_border

        ws[f'E{r}'] = sl
        ws[f'E{r}'].font = font_tbl_num
        ws[f'E{r}'].alignment = Alignment(horizontal="center", vertical="center")
        ws[f'E{r}'].border = box_border

    # Total Row Section 1
    ws.row_dimensions[16].height = 22
    ws.merge_cells('A16:D16')
    ws['A16'] = "TỔNG CỘNG"
    ws['A16'].font = font_total_lbl
    ws['A16'].fill = fill_total
    ws['A16'].alignment = Alignment(horizontal="center", vertical="center")
    for col in ['A', 'B', 'C', 'D']:
        ws[f'{col}16'].border = box_border

    ws['E16'] = "=SUM(E10:E15)"
    ws['E16'].font = font_total_num
    ws['E16'].fill = fill_total
    ws['E16'].alignment = Alignment(horizontal="center", vertical="center")
    ws['E16'].border = box_border

    # -------------------------------------------------------------
    # SECTION 4: 4. KẾ HOẠCH NHÂN LỰC NGÀY MAI (Rows 18 to 23)
    # -------------------------------------------------------------
    ws.row_dimensions[17].height = 6 # Spacer

    ws.row_dimensions[18].height = 22
    ws.merge_cells('A18:E18')
    ws['A18'] = "4. KẾ HOẠCH NHÂN LỰC NGÀY MAI (16/07/2026)"
    ws['A18'].font = font_sec_hdr
    ws['A18'].fill = fill_sec_hdr
    ws['A18'].alignment = Alignment(horizontal="left", vertical="center", indent=1)

    ws.row_dimensions[19].height = 20
    ws.merge_cells('A19:B19')
    ws['A19'] = "BỘ PHẬN / TỔ ĐỘI"
    ws['A19'].font = font_tbl_hdr
    ws['A19'].fill = fill_tbl_hdr
    ws['A19'].alignment = Alignment(horizontal="center", vertical="center")
    ws['A19'].border = box_border
    ws['B19'].border = box_border

    ws['C19'] = "NHÂN LỰC DỰ KIẾN"
    ws['C19'].font = font_tbl_hdr
    ws['C19'].fill = fill_tbl_hdr
    ws['C19'].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws['C19'].border = box_border

    ws['D19'] = "BỘ PHẬN / TỔ ĐỘI"
    ws['D19'].font = font_tbl_hdr
    ws['D19'].fill = fill_tbl_hdr
    ws['D19'].alignment = Alignment(horizontal="center", vertical="center")
    ws['D19'].border = box_border

    ws['E19'] = "NHÂN LỰC DỰ KIẾN"
    ws['E19'].font = font_tbl_hdr
    ws['E19'].fill = fill_tbl_hdr
    ws['E19'].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws['E19'].border = box_border

    sec4_data = [
        ("Ban chỉ huy công trường", 2, "Cơ giới", 4),
        ("Đội trưởng 22", 1, "Công ty Hà Thành", 8),
        ("Công nhân đội 22", 15, "Công ty Tấn Thành", 7),
    ]

    for idx, (bp1, sl1, bp2, sl2) in enumerate(sec4_data, start=1):
        r = 19 + idx
        ws.row_dimensions[r].height = 19
        ws.merge_cells(f'A{r}:B{r}')
        ws[f'A{r}'] = bp1
        ws[f'A{r}'].font = font_tbl_data
        ws[f'A{r}'].alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws[f'A{r}'].border = box_border
        ws[f'B{r}'].border = box_border

        ws[f'C{r}'] = sl1
        ws[f'C{r}'].font = font_tbl_num
        ws[f'C{r}'].alignment = Alignment(horizontal="center", vertical="center")
        ws[f'C{r}'].border = box_border

        ws[f'D{r}'] = bp2
        ws[f'D{r}'].font = font_tbl_data
        ws[f'D{r}'].alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws[f'D{r}'].border = box_border

        ws[f'E{r}'] = sl2
        ws[f'E{r}'].font = font_tbl_num
        ws[f'E{r}'].alignment = Alignment(horizontal="center", vertical="center")
        ws[f'E{r}'].border = box_border

    # Total Row Section 4
    ws.row_dimensions[23].height = 22
    ws.merge_cells('A23:D23')
    ws['A23'] = "TỔNG CỘNG"
    ws['A23'].font = font_total_num
    ws['A23'].fill = fill_total
    ws['A23'].alignment = Alignment(horizontal="right", vertical="center")
    for col in ['A', 'B', 'C', 'D']:
        ws[f'{col}23'].border = box_border

    ws['E23'] = "=SUM(C20:C22)+SUM(E20:E22)"
    ws['E23'].font = font_total_num
    ws['E23'].fill = fill_total
    ws['E23'].alignment = Alignment(horizontal="center", vertical="center")
    ws['E23'].border = box_border

    # -------------------------------------------------------------
    # SECTION 2: 2. NHÂN LỰC THEO KHU VỰC THI CÔNG (Rows 8 to 12)
    # -------------------------------------------------------------
    ws.merge_cells('G8:I8')
    ws['G8'] = "2. NHÂN LỰC THEO KHU VỰC THI CÔNG"
    ws['G8'].font = font_sec_hdr
    ws['G8'].fill = fill_sec_hdr
    ws['G8'].alignment = Alignment(horizontal="left", vertical="center", indent=1)

    # Headers for Table 2
    ws['G9'] = "KHU VỰC"
    ws['G9'].font = font_tbl_hdr
    ws['G9'].fill = fill_tbl_hdr
    ws['G9'].alignment = Alignment(horizontal="center", vertical="center")
    ws['G9'].border = box_border

    ws['H9'] = "NỘI DUNG CÔNG VIỆC"
    ws['H9'].font = font_tbl_hdr
    ws['H9'].fill = fill_tbl_hdr
    ws['H9'].alignment = Alignment(horizontal="center", vertical="center")
    ws['H9'].border = box_border

    ws['I9'] = "SỐ LƯỢNG NHÂN CÔNG"
    ws['I9'].font = font_tbl_hdr
    ws['I9'].fill = fill_tbl_hdr
    ws['I9'].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws['I9'].border = box_border

    sec2_data = [
        ("Mũi 1", "Thi công cọc khoan nhồi trụ T2", 15),
        ("Mũi 2", "Thi công bệ đúc dầm", 8),
        ("Mũi 3", "Thi công vết hàn cơ; gia công thép hào kỹ thuật", 7),
    ]

    for idx, (kv, nd, sl) in enumerate(sec2_data, start=1):
        r = 9 + idx
        ws[f'G{r}'] = kv
        ws[f'G{r}'].alignment = Alignment(horizontal="center", vertical="center")
        ws[f'G{r}'].font = font_tbl_data
        ws[f'G{r}'].border = box_border

        ws[f'H{r}'] = nd
        ws[f'H{r}'].font = font_tbl_data
        ws[f'H{r}'].alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws[f'H{r}'].border = box_border

        ws[f'I{r}'] = sl
        ws[f'I{r}'].font = font_tbl_num
        ws[f'I{r}'].alignment = Alignment(horizontal="center", vertical="center")
        ws[f'I{r}'].border = box_border

    # -------------------------------------------------------------
    # SECTION 3: 3. ĐÁNH GIÁ TÌNH HÌNH NHÂN LỰC (Rows 13 to 19)
    # -------------------------------------------------------------
    ws.row_dimensions[13].height = 22
    ws.merge_cells('G13:I13')
    ws['G13'] = "3. ĐÁNH GIÁ TÌNH HÌNH NHÂN LỰC"
    ws['G13'].font = font_sec_hdr
    ws['G13'].fill = fill_sec_hdr
    ws['G13'].alignment = Alignment(horizontal="left", vertical="center", indent=1)

    eval_items = [
        (14, '• Tổng số nhân lực hiện trường:', ' =E16 & " người."'),
        (15, '• Nhân lực đáp ứng tiến độ:', ' [x] Có     [ ] Không'),
        (16, '• Tình hình chấp hành ATLĐ:', ' [x] Tốt   [ ] Khá   [ ] Trung bình   [ ] Kém'),
        (17, '• Số nhân công mới vào công trường:', ' 00 người.'),
        (18, '• Số nhân công nghỉ việc / nghỉ phép:', ' 00 người.'),
        (19, '• Ghi chú khác:', ' ............................................................................')
    ]

    for r, label, val in eval_items:
        ws.row_dimensions[r].height = 18
        ws[f'G{r}'] = label
        ws[f'G{r}'].font = Font(name="Arial", size=9, bold=False, color="1C2430")
        ws[f'G{r}'].alignment = Alignment(horizontal="left", vertical="center")
        
        ws.merge_cells(f'H{r}:I{r}')
        if val.startswith(' ='):
            ws[f'H{r}'] = val[1:] # Formula
            ws[f'H{r}'].font = font_tbl_num
        else:
            ws[f'H{r}'] = val
            ws[f'H{r}'].font = Font(name="Arial", size=9, bold=False, color="1C2430")
        ws[f'H{r}'].alignment = Alignment(horizontal="left", vertical="center")

    # Card border for Section 3
    for r in range(14, 20):
        ws[f'G{r}'].border = Border(left=thin_border_side)
        ws[f'I{r}'].border = Border(right=thin_border_side)
    for c in ['G', 'H', 'I']:
        ws[f'{c}14'].border = Border(top=thin_border_side, left=ws[f'{c}14'].border.left, right=ws[f'{c}14'].border.right)
        ws[f'{c}19'].border = Border(bottom=thin_border_side, left=ws[f'{c}19'].border.left, right=ws[f'{c}19'].border.right)

    # -------------------------------------------------------------
    # SECTION 5: XÁC NHẬN CHỈ HUY TRƯỞNG (Rows 20 to 24)
    # -------------------------------------------------------------
    ws.row_dimensions[20].height = 20
    ws.merge_cells('G20:I20')
    ws['G20'] = "XÁC NHẬN"
    ws['G20'].font = font_sec_hdr
    ws['G20'].fill = fill_sec_hdr
    ws['G20'].alignment = Alignment(horizontal="center", vertical="center")

    ws.row_dimensions[21].height = 18
    ws.merge_cells('G21:I21')
    ws['G21'] = "CHỈ HUY TRƯỞNG CÔNG TRƯỜNG"
    ws['G21'].font = font_sub_title
    ws['G21'].alignment = Alignment(horizontal="center", vertical="center")

    # Signature row
    ws.row_dimensions[22].height = 36
    ws.merge_cells('G22:I22')
    sig_path = "/Users/hanario/Documents/quyen/assets/signature_sample.png"
    if os.path.exists(sig_path):
        sig_img = Image(sig_path)
        sig_img.width = 120
        sig_img.height = 42
        ws.add_image(sig_img, 'H22')

    ws.row_dimensions[23].height = 20
    ws.merge_cells('G23:I23')
    ws['G23'] = "Nguyễn Anh Tuấn"
    ws['G23'].font = font_sub_title
    ws['G23'].alignment = Alignment(horizontal="center", vertical="center")

    # Card border for Section 5
    for r in range(21, 24):
        ws[f'G{r}'].border = Border(left=thin_border_side)
        ws[f'I{r}'].border = Border(right=thin_border_side)
    for c in ['G', 'H', 'I']:
        ws[f'{c}23'].border = Border(bottom=thin_border_side, left=ws[f'{c}23'].border.left, right=ws[f'{c}23'].border.right)

    # -------------------------------------------------------------
    # PAGE SETUP FOR A4 LANDSCAPE PRINTING
    # -------------------------------------------------------------
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.page_margins.left = 0.3
    ws.page_margins.right = 0.3
    ws.page_margins.top = 0.3
    ws.page_margins.bottom = 0.3
    ws.page_setup.horizontalCentered = True
    ws.views.sheetView[0].showGridLines = True

    out_file = "/Users/hanario/Documents/quyen/Bao_Cao_Nhan_Luc_Hang_Ngay.xlsx"
    wb.save(out_file)
    print(f"Đã tạo thành công template Excel: {out_file}")

if __name__ == "__main__":
    create_template()
