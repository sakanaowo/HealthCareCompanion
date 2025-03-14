# Cấu trúc Project

```
📂 Project
├── 📂 data  # Thư mục lưu trữ, quản lí dữ liệu
│   ├── 📂 cache  # Thư mục lưu trữ lịch sử chat, pipeline
│   ├── 📂 images  # Thư mục chứa các hình ảnh sử dụng cho giao diện
│   ├── 📂 index_storage  # Thư mục lưu trữ quản lí index
│   ├── 📂 ingestion_storage  # Thư mục chứa dữ liệu thô
│   ├── 📂 user_storage  # Thư mục lưu trữ thông tin người dùng, kết quả đánh giá
│
├── 📂 src  # Thư mục chứa mã nguồn chính của dự án
│   ├── 📄 authenticate.py  # Module xử lí xác thực người dùng như đăng nhập, đăng ký
│   ├── 📄 conversation_engine.py  # Module tạo Agent, quản lí cuộc trò chuyện
│   ├── 📄 global_settings.py  # Module thiết lập các đường dẫn đến data
│   ├── 📄 index_builder.py  # Module tạo index
│   ├── 📄 ingest_pipeline.py  # Module tạo node
│   ├── 📄 prompts.py  # Module quản lí các prompt trong dự án
│   ├── 📄 slide_bar.py  # Module thiết lập side bar phục vụ cho việc xây dựng giao diện
│
├── 📂 pages  # Giao diện trang ứng dụng
│   ├── 📄 1_user.py  # Giao diện kết quả
│   ├── 📄 2_Chat.py  # Giao diện trò chuyện
│
├── 📂 .streamlit  # Thư mục chứa các khóa API, tùy chỉnh cấu hình streamlit
│   ├── 📄 secrets.toml  # File chứa OpenAI API key
│
├── 📄 build_data.py  # Tạo node, index và lưu trữ vào kho dữ liệu
├── 📄 evaluate.py  # Đánh giá hệ thống
├── 📄 Home.py  # Giao diện trang chủ của ứng dụng
```

