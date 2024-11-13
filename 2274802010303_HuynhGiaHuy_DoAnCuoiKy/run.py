from app import App

# Tạo một instance của App
app_instance = App()

# Khởi tạo các routes
app_instance.init_routes()

# Lấy Flask app đã cấu hình
app = app_instance.get_app()

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(debug=True)
