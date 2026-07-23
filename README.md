# how2prompt-agentic

Đây là dịch vụ tối ưu hóa prompt không trạng thái (Stateless Prompt Optimization Agent Service), đóng vai trò là backend phân tích prompt và xử lý các biến số (variables parser) cho nền tảng **how2prompt**. Dự án này áp dụng quy trình phát triển định hướng bởi đặc tả (**Spec-Driven Development - SDD**) thông qua công cụ **Spec-Kit** của GitHub.

---

## 1. Tích hợp Git Submodule

Dịch vụ này được thiết kế để nhúng trực tiếp vào dự án lớn **how2prompt** dưới dạng Git Submodule.

### Khởi tạo dự án cha kèm Submodule này
Để clone dự án cha cùng tất cả các submodule đi kèm (bao gồm cả `how2prompt-agentic`):
```bash
git clone --recurse-submodules <url-cua-project-cha>
```

### Thêm Submodule này vào dự án cha thủ công
Nếu bạn muốn thêm dự án này làm submodule vào một repo cha có sẵn:
```bash
git submodule add <url-repo-nay> how2prompt-agentic
```

### Cập nhật và đồng bộ hóa Submodule
Nếu bạn đã clone dự án cha nhưng chưa tải submodule, hãy chạy lệnh sau từ thư mục gốc của dự án cha:
```bash
git submodule update --init --recursive
```

### Cập nhật Submodule lên commit mới nhất
Để kéo các thay đổi mới nhất của subsystem này trong dự án cha:
```bash
git submodule update --remote --merge
```

---

## 2. Cấu hình Môi trường Phát triển (Spec-Kit)

Dự án này tích hợp sẵn cấu hình Spec-Kit cho các AI Coding Assistants phổ biến: **Claude Code**, **Cursor**, và **OpenCode**.

### Cài đặt Spec-Kit CLI (`specify`)
Để chạy các công cụ đặc tả và phát triển tự động, bạn cần cài đặt `specify-cli`. Lệnh khuyến nghị sử dụng `uv` (trình quản lý gói Python nhanh nhất) hoặc `pipx`:

```bash
# Cài đặt bằng uv (khuyến nghị)
uv tool install specify-cli

# Hoặc cài đặt bằng pipx
pipx install specify-cli
```
*Sau khi cài đặt, bạn có thể chạy `specify version` để xác thực.*

### Cấu hình các Integrations trong Repo
Dự án đã được tích hợp và tạo sẵn các câu lệnh / kỹ năng (Skills/Commands) cho 3 môi trường trợ lý AI:
1. **Claude Code:** Các kỹ năng được cài đặt trong thư mục `.claude/skills/`.
2. **Cursor:** Các kỹ năng được cài đặt trong thư mục `.cursor/skills/`.
3. **OpenCode:** Các câu lệnh markdown được cài đặt trong thư mục `.opencode/commands/`.

*Lưu ý: File cấu hình tổng thể của Spec-Kit nằm tại `.specify/integration.json`.*

---

## 3. Cách Sử dụng các Slash Commands (Bảng câu lệnh SDD)

Khi làm việc với các trợ lý AI hỗ trợ Spec-Kit (Claude Code, Cursor, OpenCode), bạn có thể gọi trực tiếp các câu lệnh sau để tự động hóa việc phát triển. 

*   Đối với **Claude Code** và **Cursor** (sử dụng dấu gạch ngang `-`): Ví dụ `/speckit-specify`
*   Đối với **OpenCode** (sử dụng dấu chấm `.`): Ví dụ `/speckit.specify`

| Lệnh slash | Mô tả chức năng |
| :--- | :--- |
| `/speckit.constitution` | Khởi tạo hoặc cập nhật project constitution (hiến pháp dự án) dùng chung. |
| `/speckit.specify` | Tạo hoặc cập nhật tài liệu đặc tả tính năng (`spec.md`) từ mô tả yêu cầu. |
| `/speckit.clarify` | Đưa ra các câu hỏi làm rõ các điểm mơ hồ trong tài liệu đặc tả (chạy trước khi lập kế hoạch). |
| `/speckit.plan` | Chuyển hóa đặc tả `spec.md` thành kế hoạch kỹ thuật `plan.md` (chứa Stack, Folder map, v.v.). |
| `/speckit.checklist` | Tạo danh sách các điểm kiểm thử chất lượng và phi chức năng dựa trên kế hoạch. |
| `/speckit.tasks` | Tạo danh sách tác vụ (`tasks.md`) được sắp xếp theo thứ tự phụ thuộc. |
| `/speckit.taskstoissues` | Đồng bộ danh sách tác vụ thành các GitHub Issues để quản lý công việc. |
| `/speckit.implement` | Lập trình viên AI tự động thực thi từng tác vụ tuần tự trong `tasks.md`. |
| `/speckit.analyze` | Phân tích chéo tính nhất quán và chất lượng giữa spec, kế hoạch và các task. |
| `/speckit.converge` | Đánh giá mã nguồn hiện tại so với đặc tả, phát hiện khoảng cách và tự động tạo task bù đắp. |

---

## 4. Cấu trúc thư mục Spec-Kit

Toàn bộ các tài liệu đặc tả và cấu hình của Spec-Kit được tổ chức khoa học bên trong thư mục ẩn `.specify/` để giữ gốc repo sạch sẽ:

```text
how2prompt-agentic/
├── .claude/skills/            # Tích hợp skills dành riêng cho Claude Code
├── .cursor/skills/            # Tích hợp skills dành riêng cho Cursor
├── .opencode/commands/        # Các file lệnh markdown dành riêng cho OpenCode
├── .specify/
│   ├── integration.json       # File cấu hình các assistant đang được cài đặt
│   ├── init-options.json      # File ghi nhận tùy chọn khởi tạo dự án
│   ├── memory/
│   │   └── constitution.md    # Hiến pháp dự án - nguồn sự thật tối cao về kiến trúc
│   ├── templates/
│   │   └── overrides/         # Chứa các template kế hoạch và task được tùy biến
│   └── specs/
│       └── how2prompt-mvp/    # Các tài liệu đặc tả của tính năng MVP hiện tại
│           ├── spec.md        # Yêu cầu nghiệp vụ & Given-When-Then test cases
│           ├── plan.md        # Kế hoạch kiến trúc hệ thống
│           └── tasks.md       # Danh sách tác vụ phát triển & test
```

---

## 5. Sử dụng Workspace đa dự án (Code Workspace)

Để thuận tiện phát triển đồng thời cả dự án cha **how2prompt** và submodule **how2prompt-agentic** trong VS Code / Cursor / OpenCode, hãy mở file cấu hình workspace nằm ở thư mục gốc của dự án cha:

*   **Đường dẫn file:** `how2prompt.code-workspace`
*   Workspace này đã gom sẵn cấu trúc thư mục cha - con và cấu hình loại trừ (exclude) các file metadata ẩn để giao diện Explorer sạch sẽ nhất.

---

## 6. Yêu cầu Hệ thống (Chạy local)
* Python ^3.11
* Poetry ^1.8

---
*Bản quyền phát triển thuộc về Spec Kit & How2Prompt Team.*
