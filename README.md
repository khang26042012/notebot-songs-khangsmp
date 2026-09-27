# 🎵 Kho Nhạc NoteBot NBS & Tool Chuyển Đổi Tự Động (Meteor Client)

Kho lưu trữ các bản nhạc định dạng **.NBS (Open Note Block Studio)** được tối ưu hóa đặc biệt dành riêng cho module **NoteBot** của **Meteor Client**, tương thích hoàn hảo với máy chủ Minecraft KhangSMP.

---

## 🎧 Danh Sách Nhạc Có Sẵn Trong Thư Mục `songs/`

| Tên Bài Hát | Tác Giả / Phong Cách | Độ Khó NoteBot | File Tải Về |
| :--- | :--- | :---: | :--- |
| **Nơi Này Có Anh** | Sơn Tùng M-TP | Dễ (10 TPS) | [`songs/Noi_Nay_Co_Anh.nbs`](songs/Noi_Nay_Co_Anh.nbs) |
| **Heavenly (Jumpstyle Remix)** | Jumpstyle / Hardstyle Trance | Cao (14 TPS) | [`songs/Heavenly_Jumpstyle.nbs`](songs/Heavenly_Jumpstyle.nbs) |
| **Cause I Love You** | Noo Phước Thịnh | Trung Bình (12 TPS) | [`songs/Cause_I_Love_You.nbs`](songs/Cause_I_Love_You.nbs) |

---

## 🛡️ Tính Năng Chống Ban Anti-Cheat Vulcan (Vulcan-Safe Mode)
- **Giới hạn số nốt đồng thời (Polyphony Limiter):** Tối đa 2 - 3 nốt trên 1 game tick, loại bỏ hoàn toàn các lỗi `FastClick` / `InteractSpam` của Vulcan Anti-Cheat.
- **Dịch nốt tự động (Octave Clamping):** Toàn bộ các nốt nhạc được chuyển về dải 2 quãng tám hợp lệ của Minecraft (F#3 đến F#5, tương ứng key 33 - 57), không gây crash client.
- **Tự động gán nhạc cụ theo âm sắc:**
  - Tiếng Trầm $	o$ **Double Bass (Đặt trên khối Gỗ)**
  - Tiếng Trung $	o$ **Harp / Piano (Đặt trên khối Đất)**
  - Tiếng Cao / Giai điệu bay bổng $	o$ **Bell / Chime (Đặt trên khối Vàng / Băng)**
  - Tiếng Trống $	o$ **Bass Drum (Đá)** và **Snare (Cát)**

---

## 🚀 Hướng Dẫn Sử Dụng Trực Tiếp Trên GitHub Actions (Không Cần Cài Đặt)

1. Vào tab **Actions** của repository: [`Convert Audio / YouTube to NBS`](https://github.com/khang26042012/notebot-songs-khangsmp/actions/workflows/convert.yml).
2. Bấm vào nút **Run workflow**.
3. Điền các thông tin:
   - **audio_url:** Link YouTube bất kỳ hoặc link trực tiếp tệp MP3 / MIDI.
   - **song_name:** Tên bài hát muốn xuất ra.
   - **target_tps:** 20 (chuẩn) hoặc 10 (chậm, êm tai).
   - **vulcan_safe:** Giữ nguyên `true` để an toàn chống ban.
4. Chờ GitHub Actions chạy (khoảng 30 - 45 giây), sau đó:
   - File `.nbs` sẽ tự động được lưu vào thư mục `songs/`.
   - Hoặc tải trực tiếp từ mục **Artifacts** ở cuối trang chạy của Action!

---

## 🎮 Cách Bỏ Vào Game Để NoteBot Tự Đánh Ingame

1. Tải file `.nbs` về máy tính.
2. Bỏ file vào thư mục NoteBot của Meteor Client:
   ```text
   .minecraft/meteor-client/notebot/
   ```
3. Vào game, mở menu **Meteor Client (phím RSHIFT)** $	o$ tìm module **NoteBot**:
   - Chọn bài hát trong danh sách tải lên.
   - Bấm **Load Song** và đứng cạnh dàn Note Block để máy tự động gõ nhạc biểu diễn!
