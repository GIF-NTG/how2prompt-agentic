# Tài liệu Đặc tả Yêu cầu Phần mềm (SRS) — How2Prompt Web App

Tài liệu này gộp toàn bộ các thông tin từ PRD, Phụ lục kỹ thuật, Tài liệu giải pháp và Phân rã User Stories thành một tài liệu Đặc tả Yêu cầu Phần mềm (SRS) duy nhất cho dự án **How2Prompt**.

---

## 1. Giới thiệu & Tầm nhìn (Introduction & Vision)

### 1.1 Tầm nhìn Sản phẩm (Product Vision)
**How2Prompt** là một ứng dụng web tối giản được thiết kế để huấn luyện và nâng cao kỹ năng viết prompt cho người dùng thông qua việc thực hành cấu trúc prompt chuẩn chỉnh (bao gồm 3 thành phần cốt lõi: **Vai trò - Role, Bối cảnh - Context, Ràng buộc - Constraints**).

Thay vì cung cấp các prompt viết sẵn hoàn chỉnh khiến người dùng lười tư duy, How2Prompt chỉ cung cấp các **mẫu cấu trúc trống (Empty Templates)** đi kèm hướng dẫn. Người dùng trực tiếp tương tác, điền thông tin thực tế của mình vào các ô trống (placeholders) để tạo ra prompt chất lượng cao để copy.

### 1.2 Đối tượng Người dùng & Jobs To Be Done
* **Khách (Guest):** Người dùng vãng lai chưa đăng ký tài khoản. Nhiệm vụ cần thực hiện (JTBD) là duyệt danh mục, điền placeholder và copy nhanh prompt mà không cần tạo tài khoản.
* **Thành viên (Member):** Người dùng đã đăng nhập. JTBD là lưu trữ tự động lịch sử các lần prompt để tái sử dụng nhanh chóng và xóa lịch sử khi không cần thiết.

### 1.3 Mục tiêu ngoài phạm vi (Non-Goals)
* Không tích hợp cửa sổ chat trực tiếp với AI (ChatGPT, Gemini, v.v.) trên ứng dụng How2Prompt.
* Không đồng bộ đám mây (Cloud Sync) cho đối tượng Khách (Guest).
* Không tự động sinh template bằng AI (AI Template Recommendation).

---

## 2. Hành trình Người dùng Cốt lõi (Key User Journeys)

* **UJ-1: Nam (Khách chưa đăng nhập) điền placeholder trực tiếp và sao chép prompt.**
  * *Bối cảnh:* Nam, lập trình viên muốn viết prompt báo cáo lỗi tốt hơn.
  * *Hành trình:* Vào trang chủ ➔ Chọn template debug ➔ Điền inline trực tiếp các placeholder ➔ Nhấn "Hoàn thành" ➔ Hệ thống sinh prompt đầy đủ ➔ Bấm "Sao chép nhanh" ➔ Dán vào AI chat ngoài.
* **UJ-2: Minh (Thành viên đã đăng nhập) sử dụng prompt và xem lại lịch sử.**
  * *Bối cảnh:* Minh, QA muốn tái sử dụng các prompt viết test case cũ.
  * *Hành trình:* Đăng nhập ➔ Tạo prompt ở trang chủ (tự động lưu vào DB) ➔ Vào trang "Lịch sử" ➔ Tìm prompt cũ ➔ Bấm "Copy nhanh" trên dòng lịch sử mà không cần điền lại.

---

## 3. Danh sách Yêu cầu Hệ thống

### 3.1 Yêu cầu Chức năng (Functional Requirements - FRs)
* **FR-1:** Hiển thị danh sách các Template trống dưới dạng các thẻ (cards).
* **FR-2:** Lọc danh sách template theo các nút Tag/Filter chủ đề (ví dụ: `#debugging`, `#marketing`).
* **FR-3:** Tìm nhanh template dựa trên ô tìm kiếm từ khóa.
* **FR-4:** Hiển thị các trường placeholder trống dạng input inline nằm trực tiếp trong cấu trúc câu của template.
* **FR-5:** Ô nhập liệu inline tự động co giãn chiều rộng (auto-resize width) theo độ dài chữ gõ.
* **FR-6:** Tự động lưu các giá trị đang điền vào `localStorage` của trình duyệt.
* **FR-7:** Nút "Reset" để xóa sạch dữ liệu đã điền trong template đang chọn.
* **FR-8:** Nút "Hoàn thành" để ghép các giá trị placeholder với phần chữ tĩnh sinh ra Đoạn Prompt hoàn chỉnh.
* **FR-9:** Nút "Sao chép" (Copy) bên cạnh Đoạn Prompt hoàn chỉnh kèm toast "Đã sao chép" trong 2 giây.
* **FR-10:** Ràng buộc điền đầy đủ placeholder khi bấm "Hoàn thành" (ngăn kết xuất, highlight đỏ và focus).
* **FR-11:** Đăng ký tài khoản mới và đăng nhập thành viên.
* **FR-12:** Đăng xuất tài khoản an toàn.
* **FR-13:** Duy trì phiên đăng nhập của người dùng qua JWT token lưu ở localStorage.
* **FR-14:** Tự động lưu prompt hoàn chỉnh, tên template, các giá trị và thời gian tạo vào Postgres cho Member.
* **FR-15:** Xem danh sách các lần prompt trước đó trong trang Lịch sử, sắp xếp mới nhất.
* **FR-16:** Nút "Copy nhanh" trên mỗi dòng lịch sử để sao chép trực tiếp.
* **FR-17:** Xóa từng bản ghi lịch sử prompt khỏi cơ sở dữ liệu.

### 3.2 Yêu cầu Phi chức năng (Non-Functional Requirements - NFRs)
* **NFR-1 (Hiệu năng):** Thao tác gõ của người dùng trên ô input inline phải phản hồi tức thì (< 50ms), chiều rộng ô tự co giãn mượt mà.
* **NFR-2 (Tương thích):** Chạy tốt trên Chrome, Safari, Edge, và Firefox (Desktop & Mobile).
* **NFR-3 (Bảo mật):** Mật khẩu người dùng được băm (hash) bằng BCrypt trước khi lưu. JWT truyền tải qua kênh bảo mật HTTPS.

---

## 4. Thiết kế Kỹ thuật & Cơ sở Dữ liệu

### 4.1 Công nghệ Sử dụng
* **Frontend:** React (SPA, Vite), Axios gọi API, React Context API quản lý trạng thái đăng nhập.
* **Backend:** Java Spring Boot 3.2.x, JPA/Hibernate kết nối DB, Spring Security + JWT Filter bảo mật.
* **Database:** PostgreSQL 15.x.

### 4.2 Thiết kế Cơ sở Dữ liệu (Database Schema)

* Bảng **`users`** (Khóa chính UUID): Lưu thông tin email, username, password_hash.
* Bảng **`prompt_templates`** (Khóa chính UUID): Lưu tiêu đề template, mô tả cấu trúc, raw_template (chứa cú pháp placeholder `{ten_truong}`) và mảng tags.
* Bảng **`prompt_histories`** (Khóa chính UUID, khóa ngoại `user_id` và `template_id`): Lưu `filled_values` (JSONB) và `generated_prompt` (TEXT). Đánh index trên `(user_id, created_at DESC)`.

### 4.3 Đặc tả REST API
* `POST /api/auth/register` - Đăng ký tài khoản.
* `POST /api/auth/login` - Đăng nhập nhận JWT Token (hạn 7 ngày).
* `GET /api/templates` - Lấy danh mục template trống (công khai).
* `GET /api/histories` - Lấy danh sách lịch sử prompt của Member (yêu cầu JWT).
* `POST /api/histories` - Lưu lịch sử prompt của Member (yêu cầu JWT).
* `DELETE /api/histories/{id}` - Xóa bản ghi lịch sử prompt của Member (yêu cầu JWT).

---

## 5. Phân rã Epics & Stories Chi tiết

### Epic 1: Trình tạo và Sao chép Prompt tối giản
* **Story 1.1: Tạo khung dự án & Hiển thị danh mục Template trống từ DB**
  * *Acceptance Criteria:* API `GET /api/templates` hoạt động tốt. React kết xuất danh sách template dạng thẻ (cards) hiển thị tiêu đề, mô tả và tag.
* **Story 1.2: Lọc theo Tag và Tìm kiếm Template**
  * *Acceptance Criteria:* Bấm tag filter danh sách động; Nhập ô tìm kiếm lọc template có tiêu đề/mô tả chứa từ khóa.
* **Story 1.3: Trình soạn thảo điền Inline với tự co giãn ô nhập liệu**
  * *Acceptance Criteria:* Các placeholder hiển thị dạng input text inline trong dòng câu. Người dùng gõ chữ, ô input tự co giãn kích thước (auto-resize width) khớp với độ dài ký tự thực tế.
* **Story 1.4: Tự động lưu LocalStorage & Nút Reset**
  * *Acceptance Criteria:* Đóng tab/F5 trang React tự khôi phục dữ liệu từ LocalStorage. Bấm "Reset" xóa sạch dữ liệu placeholders của template hiện tại.
* **Story 1.5: Kết xuất Prompt hoàn chỉnh & Sao chép nhanh**
  * *Acceptance Criteria:* Điền đủ bấm "Hoàn thành" sinh prompt ghép chữ. Bấm "Sao chép" copy vào clipboard và hiển thị toast 2 giây. Thiếu ô bắt buộc, ngăn sinh prompt, highlight đỏ và focus ô trống đầu tiên.

### Epic 2: Xác thực & Quản lý Tài khoản
* **Story 2.1: Đăng ký tài khoản Member**
  * *Acceptance Criteria:* Tạo bảng `users`. API `POST /api/auth/register` hoạt động tốt (băm mật khẩu BCrypt). Giao diện React đăng ký thành công chuyển hướng về `/login`.
* **Story 2.2: Đăng nhập tài khoản & Nhận JWT Token**
  * *Acceptance Criteria:* API `POST /api/auth/login` kiểm tra mật khẩu, sinh JWT Token. Sai tài khoản trả về `401 Unauthorized` có định dạng lỗi JSON chuẩn.
* **Story 2.3: Duy trì phiên đăng nhập & Đăng xuất an toàn**
  * *Acceptance Criteria:* Có token, React lưu LocalStorage và cập nhật trạng thái `AuthContext`. F5 trang tự khôi phục phiên đăng nhập. Bấm "Đăng xuất" xóa token, xóa context và về trang chủ.

### Epic 3: Lưu trữ & Quản lý Lịch sử Prompt
* **Story 3.1: Tự động ghi nhận Lịch sử Prompt khi tạo thành công**
  * *Acceptance Criteria:* Tạo bảng `prompt_histories`. Khi Member bấm "Hoàn thành", React gửi `POST /api/histories` đính kèm JWT header. Service Spring Boot lưu thông tin thành công trong phương thức `@Transactional`.
* **Story 3.2: Xem danh sách Lịch sử Prompt**
  * *Acceptance Criteria:* Vào trang Lịch sử gọi `GET /api/histories` (có JWT header) lấy lịch sử sắp xếp mới nhất hiển thị lên React.
* **Story 3.3: Sao chép nhanh từ Lịch sử & Xóa lịch sử**
  * *Acceptance Criteria:* Bấm "Copy nhanh" trên dòng lịch sử sao chép prompt trực tiếp. Bấm "Xóa" gọi `DELETE /api/histories/{id}` xóa dữ liệu trong DB và gỡ khỏi danh sách React.

---

## 6. Thuật ngữ (Glossary)
* **Template trống (Empty Template):** Bản thiết kế cấu trúc prompt chứa các câu lệnh định hướng cố định kết hợp với các ô trống (Placeholder Field).
* **Trường nhập liệu (Placeholder Field):** Ô trống được định nghĩa sẵn trong template để người dùng click vào và điền giá trị cụ thể.
* **Điền trực tiếp (Inline Filling):** Trải nghiệm nhập văn bản trực tiếp ngay trên dòng của template.
* **Đoạn Prompt hoàn chỉnh (Generated Prompt):** Kết quả văn bản cuối cùng được tạo ra bằng cách ghép các giá trị người dùng đã điền vào đúng vị trí trong Template trống.
* **Sao chép nhanh (Quick Copy):** Hành động sao chép Đoạn Prompt hoàn chỉnh vào clipboard chỉ bằng một click chuột.
* **Bộ lọc nhanh (Quick Filters/Tags):** Cơ chế lọc các Template trống theo chủ đề.
