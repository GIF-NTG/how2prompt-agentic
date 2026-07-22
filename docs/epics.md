# How2Prompt - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for How2Prompt, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

* **FR-1:** Hệ thống hiển thị danh sách các Template trống dưới dạng các thẻ (cards). Mỗi thẻ hiển thị tiêu đề, các thẻ tag phân loại và 2-3 dòng giải thích ngắn về cấu trúc/mục đích của template đó.
* **FR-2:** Người dùng có thể lọc danh sách template bằng cách nhấn vào các nút Tag/Filter chủ đề (ví dụ: `#debugging`, `#marketing`, `#writing`).
* **FR-3:** Hệ thống cung cấp ô tìm kiếm giúp người dùng tìm nhanh template dựa trên tiêu đề hoặc mô tả của template.
* **FR-4:** Hệ thống hiển thị các trường placeholder trống dạng input inline nằm trực tiếp trong cấu trúc câu của template.
* **FR-5:** Ô nhập liệu inline (input) phải tự động thay đổi chiều rộng (auto-resize width) theo độ dài của ký tự khi người dùng gõ để tránh làm vỡ bố cục câu văn của template.
* **FR-6:** Hệ thống tự động lưu các giá trị người dùng đang nhập vào `localStorage` theo từng template. Nếu người dùng tải lại trang (F5) hoặc vô tình đóng trình duyệt, khi quay lại các trường đã điền vẫn được giữ nguyên.
* **FR-7:** Hệ thống cung cấp nút "Reset" (Xóa sạch) để người dùng nhanh chóng xóa toàn bộ dữ liệu đã nhập trong các placeholder của template hiện tại về trạng thái trống ban đầu.
* **FR-8:** Khi người dùng nhấn nút "Hoàn thành" (Complete), hệ thống sẽ ghép các giá trị trong các placeholder vào đúng vị trí của template tĩnh để tạo ra Đoạn Prompt hoàn chỉnh, hiển thị trong một khu vực (textarea/code block) riêng biệt.
* **FR-9:** Hệ thống hiển thị một nút "Sao chép" (Copy) bên cạnh Đoạn Prompt hoàn chỉnh. Khi click, prompt sẽ được sao chép vào clipboard và hệ thống hiển thị thông báo "Đã sao chép" (Copied!) trực quan dưới dạng toast hoặc tooltip biến mất sau 2 giây.
* **FR-10:** Nếu người dùng nhấn "Hoàn thành" khi vẫn còn ít nhất một trường placeholder bắt buộc chưa điền, hệ thống sẽ ngăn việc kết xuất prompt, highlight đỏ các trường trống đó và tự động cuộn màn hình (focus) về trường trống đầu tiên.
* **FR-11:** Người dùng có thể đăng ký tài khoản mới (bằng Email, Tên hiển thị, Mật khẩu) và đăng nhập vào hệ thống.
* **FR-12:** Người dùng có thể đăng xuất để hủy phiên làm việc an toàn.
* **FR-13:** Hệ thống giữ trạng thái đăng nhập của người dùng qua JWT token (hoặc cơ chế tương đương) được lưu trong cookie hoặc localStorage.
* **FR-14:** Khi Member bấm "Hoàn thành" để kết xuất prompt, hệ thống tự động ghi nhận và lưu thông tin prompt hoàn chỉnh, tên template, các giá trị placeholder đã điền, và thời gian tạo vào cơ sở dữ liệu PostgreSQL.
* **FR-15:** Member có thể truy cập trang Lịch sử để xem danh sách các lần prompt trước đó, sắp xếp theo thời gian mới nhất.
* **FR-16:** Mỗi bản ghi lịch sử có một nút "Copy nhanh" để Member sao chép trực tiếp prompt đó mà không cần vào lại template.
* **FR-17:** Member có thể xóa từng bản ghi lịch sử prompt của mình khỏi cơ sở dữ liệu.

### NonFunctional Requirements

* **NFR-1:** Hiệu năng giao diện (UX Performance): Thao tác gõ trên ô input inline phản hồi tức thì (< 50ms), chiều rộng ô tự co giãn mượt mà.
* **NFR-2:** Khả năng tương thích trình duyệt (Browser Compatibility): Tương thích tốt trên Chrome, Safari, Edge, Firefox (Desktop và Mobile).
* **NFR-3:** Bảo mật dữ liệu tài khoản: Mật khẩu người dùng được băm (hash) bằng BCrypt trước khi lưu vào PostgreSQL. JWT token truyền tải qua kênh bảo mật HTTPS.

### Additional Requirements

* **AR-1 (Tech Stack):** Sử dụng các phiên bản: Java 17, Spring Boot 3.2.x, PostgreSQL 15.x, React 18.x, Axios 1.6.x, Node.js 20.x.
* **AR-2 (Database Schema):** Bảng cơ sở dữ liệu `users`, `prompt_templates`, `prompt_histories` sử dụng UUID làm khóa chính (Primary Key). Đánh index trên `(user_id, created_at DESC)` cho bảng lịch sử prompt.
* **AR-3 (API RESTful):** Định dạng ngày tháng ISO 8601 (`YYYY-MM-DDTHH:mm:ssZ`), cấu trúc lỗi thống nhất `{"status": Int, "error": String, "message": String}`.
* **AR-4 (Backend MVC Flow):** Tuân thủ luồng phụ thuộc một chiều: Controller ➔ Service ➔ Repository ➔ Entity.
* **AR-5 (Transaction Boundary):** Bắt buộc sử dụng `@Transactional` ở mức Service Layer cho tất cả các tác vụ thay đổi dữ liệu (write operations).
* **AR-6 (JWT Session LocalStorage):** Token JWT phiên đăng nhập được lưu ở LocalStorage, thời hạn 7 ngày.
* **AR-7 (Axios API Client):** Sử dụng Axios instance tập trung với Request Interceptor gắn token và Response Interceptor bắt lỗi 401 chuyển về trang Login.
* **AR-8 (React Auto-Resize):** Lập trình React Auto-resize ô input inline sử dụng thẻ span ẩn để đo độ rộng chữ.

### UX Design Requirements

*Không có.*

### FR Coverage Map

* **FR-1:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-2:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-3:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-4:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-5:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-6:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-7:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-8:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-9:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-10:** Epic 1 - Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
* **FR-11:** Epic 2 - Xác thực & Quản lý Tài khoản (Authentication & User Accounts)
* **FR-12:** Epic 2 - Xác thực & Quản lý Tài khoản (Authentication & User Accounts)
* **FR-13:** Epic 2 - Xác thực & Quản lý Tài khoản (Authentication & User Accounts)
* **FR-14:** Epic 3 - Lưu trữ & Quản lý Lịch sử Prompt (Prompt History)
* **FR-15:** Epic 3 - Lưu trữ & Quản lý Lịch sử Prompt (Prompt History)
* **FR-16:** Epic 3 - Lưu trữ & Quản lý Lịch sử Prompt (Prompt History)
* **FR-17:** Epic 3 - Lưu trữ & Quản lý Lịch sử Prompt (Prompt History)

## Epic List

### Epic 1: Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)
Cho phép người dùng (cả Khách và Thành viên) có thể tìm kiếm, lọc các template trống, điền các giá trị placeholder trực tiếp (inline), tự động lưu trữ tạm thời và xuất/copy đoạn prompt hoàn chỉnh.
**FRs covered:** FR-1, FR-2, FR-3, FR-4, FR-5, FR-6, FR-7, FR-8, FR-9, FR-10.

### Epic 2: Xác thực & Quản lý Tài khoản (Authentication & User Accounts)
Cho phép người dùng đăng ký, đăng nhập, duy trì phiên đăng nhập JWT bảo mật để chuyển từ trạng thái Khách sang Thành viên (Member).
**FRs covered:** FR-11, FR-12, FR-13.

### Epic 3: Lưu trữ & Quản lý Lịch sử Prompt (Prompt History)
Tự động ghi nhận các lần tạo prompt thành công của Member vào database PostgreSQL, hỗ trợ xem lại danh sách lịch sử, copy nhanh hoặc xóa lịch sử.
**FRs covered:** FR-14, FR-15, FR-16, FR-17.

## Epic 1: Trình tạo và Sao chép Prompt tối giản (Core Prompt Construction Utility)

Mục tiêu: Cho phép người dùng (cả Khách và Thành viên) có thể tìm kiếm, lọc các template trống, điền các giá trị placeholder trực tiếp (inline), tự động lưu trữ tạm thời và xuất/copy đoạn prompt hoàn chỉnh.

### Story 1.1: Tạo khung dự án & Hiển thị danh mục Template trống từ DB
As a Khách,
I want to see a catalog of empty prompt templates,
So that I can browse available templates.

**Acceptance Criteria:**
* **Given** database PostgreSQL đã chạy và chứa dữ liệu bảng `prompt_templates` (gồm ID (UUID), tiêu đề, mô tả, template tĩnh và tag).
* **When** người dùng truy cập trang chủ của ứng dụng.
* **Then** hệ thống thực hiện gọi API `/api/templates` (Spring Boot) để lấy danh sách.
* **And** hiển thị danh sách các template trống dưới dạng các thẻ (cards) hiển thị đầy đủ tiêu đề, mô tả và tag.

### Story 1.2: Lọc theo Tag và Tìm kiếm Template
As a Khách,
I want to filter templates by tags and search them by keywords,
So that I can find a specific template quickly.

**Acceptance Criteria:**
* **Given** danh sách danh mục template đang hiển thị trên trang chủ.
* **When** người dùng nhấp vào một nút Tag/Filter chủ đề (ví dụ: `#debugging`).
* **Then** danh mục hiển thị thay đổi động, chỉ hiển thị các template có tag tương ứng.
* **When** người dùng nhập từ khóa tìm kiếm vào ô Search.
* **Then** hệ thống tự động lọc các template có tiêu đề hoặc mô tả chứa từ khóa đó.

### Story 1.3: Trình soạn thảo điền Inline với tự co giãn ô nhập liệu
As a Khách,
I want to click and fill in placeholder fields inline directly inside the template text,
So that I can build my prompt context intuitively.

**Acceptance Criteria:**
* **Given** người dùng đã chọn một thẻ template để soạn thảo.
* **When** template hiển thị, các trường placeholder (ví dụ: `[Môi trường]`) được kết xuất dạng input text inline nằm ngay trong dòng câu của template.
* **When** người dùng nhập dữ liệu vào ô input inline.
* **Then** ô input tự động thay đổi chiều rộng (auto-resize width) khớp với độ rộng thực tế của ký tự đang gõ, đảm bảo văn bản hiển thị tự nhiên.

### Story 1.4: Tự động lưu LocalStorage & Nút Reset
As a Khách,
I want my filled placeholders to auto-save to browser local storage and be able to clear them,
So that I don't lose progress and can easily start over.

**Acceptance Criteria:**
* **Given** người dùng đang điền các giá trị vào placeholder của template.
* **When** người dùng thực hiện tải lại trang (F5) hoặc vô tình đóng trình duyệt và mở lại.
* **Then** React tự động khôi phục các giá trị đã điền trước đó từ `localStorage`.
* **When** người dùng bấm nút "Reset" (Xóa sạch).
* **Then** hệ thống xóa toàn bộ dữ liệu đã nhập trong các placeholder của template hiện tại trong cả React State và `localStorage`.

### Story 1.5: Kết xuất Prompt hoàn chỉnh & Sao chép nhanh
As a Khách,
I want to generate the complete prompt and copy it with one click,
So that I can paste it into an AI chat.

**Acceptance Criteria:**
* **Given** người dùng đang soạn thảo trên một template.
* **When** người dùng bấm nút "Hoàn thành" (Complete) và tất cả các trường placeholder bắt buộc đã được điền.
* **Then** hệ thống ghép các giá trị trong placeholder với phần tĩnh của template để sinh ra Đoạn Prompt hoàn chỉnh hiển thị trong một khung riêng biệt.
* **When** người dùng click nút "Sao chép" (Copy).
* **Then** đoạn prompt được lưu vào clipboard, đồng thời hiển thị thông báo "Đã sao chép!" (toast/tooltip) trong 2 giây rồi tự động biến mất.
* **When** người dùng bấm "Hoàn thành" nhưng vẫn còn ít nhất một ô placeholder bắt buộc để trống.
* **Then** hệ thống ngăn chặn việc sinh prompt, highlight đỏ viền ô input trống và tự động cuộn màn hình (focus) về ô trống đầu tiên.

## Epic 2: Xác thực & Quản lý Tài khoản (Authentication & User Accounts)

Mục tiêu: Cho phép người dùng đăng ký, đăng nhập, duy trì phiên đăng nhập JWT bảo mật để chuyển từ trạng thái Khách sang Thành viên (Member).

### Story 2.1: Đăng ký tài khoản Member
As a Khách,
I want to đăng ký một tài khoản mới,
So that tôi có thể truy cập các tính năng lưu lịch sử prompt.

**Acceptance Criteria:**
* **Given** database PostgreSQL đã chạy và chứa cấu trúc bảng `users` (gồm ID (UUID), email (unique), username, password_hash và created_at).
* **When** người dùng gửi biểu mẫu đăng ký gồm email, username và mật khẩu hợp lệ.
* **Then** backend kiểm tra email không trùng lặp, thực hiện băm mật khẩu bằng BCrypt và lưu vào bảng `users`.
* **And** trả về thông báo thành công và React chuyển hướng người dùng sang trang `/login`.

### Story 2.2: Đăng nhập tài khoản & Nhận JWT Token
As a Khách,
I want to đăng nhập bằng email và mật khẩu của mình,
So that tôi có thể xác thực phiên làm việc.

**Acceptance Criteria:**
* **Given** người dùng đã đăng ký tài khoản thành công.
* **When** người dùng gửi biểu mẫu đăng nhập với email và mật khẩu chính xác.
* **Then** Spring Boot API `/api/auth/login` thực hiện kiểm tra mật khẩu qua BCrypt, tạo và trả về mã JWT Token (thời hạn 7 ngày).
* **When** người dùng nhập sai email hoặc mật khẩu.
* **Then** API trả về mã lỗi `401 Unauthorized` có cấu trúc JSON lỗi chuẩn: `{"status": 401, "error": "Unauthorized", "message": "Email hoặc mật khẩu không chính xác"}`.

### Story 2.3: Duy trì phiên đăng nhập & Đăng xuất an toàn
As a Member,
I want phiên đăng nhập được duy trì lâu dài và có thể đăng xuất an toàn,
So that tôi không phải nhập lại tài khoản liên tục và có thể bảo mật thông tin khi rời máy.

**Acceptance Criteria:**
* **Given** người dùng đăng nhập thành công và React nhận được JWT Token.
* **When** nhận được token, React thực hiện lưu trữ vào `localStorage` và cập nhật trạng thái `AuthContext` (Navbar cập nhật tên user và nút "Đăng xuất").
* **When** người dùng thực hiện tải lại trang (F5) hoặc mở lại tab.
* **Then** React tự động lấy token từ `localStorage`, xác thực phiên đăng nhập vẫn còn hiệu lực.
* **When** người dùng bấm nút "Đăng xuất".
* **Then** hệ thống xóa token khỏi `localStorage`, đặt trạng thái `AuthContext` về `null` và chuyển hướng người dùng về trang chủ.

## Epic 3: Lưu trữ & Quản lý Lịch sử Prompt (Prompt History)

Mục tiêu: Tự động ghi nhận các lần tạo prompt thành công của Member vào database PostgreSQL, hỗ trợ xem lại danh sách lịch sử, copy nhanh hoặc xóa lịch sử.

### Story 3.1: Tự động ghi nhận Lịch sử Prompt khi tạo thành công
As a Member,
I want to tự động lưu các prompt đã tạo vào tài khoản của mình,
So that tôi có thể xem lại và sử dụng chúng sau này.

**Acceptance Criteria:**
* **Given** database PostgreSQL đã chạy và chứa cấu trúc bảng `prompt_histories` (gồm ID (UUID), user_id (FK), template_id (FK), filled_values (JSONB), generated_prompt (TEXT) và created_at).
* **When** một Member (đã đăng nhập) điền hoàn tất placeholder và bấm nút "Hoàn thành" (FR-8).
* **Then** React gửi yêu cầu `POST /api/histories` đính kèm JWT header.
* **And** Spring Boot Service thực hiện lưu thông tin prompt đó vào bảng `prompt_histories` thông qua một Service Method có cấu hình `@Transactional`.
* **And** hệ thống hiển thị thông báo "Đã lưu lịch sử prompt".

### Story 3.2: Xem danh sách Lịch sử Prompt
As a Member,
I want to xem danh sách các lần prompt cũ của mình,
So that tôi có thể rà soát lại hoạt động viết prompt.

**Acceptance Criteria:**
* **Given** Member đã đăng nhập và đang ở trang chủ.
* **When** người dùng nhấp vào mục "Lịch sử" trên thanh điều hướng.
* **Then** React gọi API `GET /api/histories` đính kèm JWT header.
* **And** Spring Boot API truy vấn và trả về danh sách lịch sử của người dùng đăng nhập hiện tại, sắp xếp theo thời gian mới nhất (sử dụng chỉ mục `(user_id, created_at DESC)` để đảm bảo hiệu năng).
* **And** React hiển thị danh sách này một cách trực quan, ghi nhận rõ tiêu đề template, thời gian tạo và đoạn prompt đã kết xuất.

### Story 3.3: Sao chép nhanh từ Lịch sử & Xóa lịch sử
As a Member,
I want to sao chép nhanh prompt cũ hoặc xóa bản ghi lịch sử,
So that tôi có thể tái sử dụng ngay lập tức hoặc dọn dẹp các prompt không cần thiết.

**Acceptance Criteria:**
* **Given** danh sách lịch sử prompt đang được hiển thị trên trang Lịch sử.
* **When** người dùng nhấp vào nút "Copy nhanh" trên một dòng lịch sử.
* **Then** hệ thống sao chép trực tiếp đoạn prompt hoàn chỉnh đó vào clipboard của hệ điều hành và hiển thị thông báo đã sao chép.
* **When** người dùng nhấp vào nút "Xóa" trên một dòng lịch sử.
* **Then** React gửi yêu cầu `DELETE /api/histories/{id}` lên backend.
* **And** Spring Boot thực hiện xóa bản ghi có ID tương ứng trong bảng `prompt_histories` và React cập nhật giao diện loại bỏ dòng lịch sử đó ngay lập tức.



