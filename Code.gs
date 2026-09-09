/**
 * Web App Báo Cáo Nhân Lực Hàng Ngày - CIENCO 510
 * Chạy trên Google Drive / Google Apps Script
 */

function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Báo Cáo Nhân Lực Hàng Ngày - CIENCO 510')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
