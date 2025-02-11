پایپ‌لاین داده Apache Airflow
این پروژه یک پایپ‌لاین داده در Apache Airflow است که داده‌های PostgreSQL را خوانده و در AWS S3 یا MinIO ذخیره می‌کند. این سیستم با استفاده از Docker Compose راه‌اندازی شده و شامل PostgreSQL، Airflow Webserver، Scheduler و Worker است.
📌 ویژگی‌ها
•	استخراج داده از PostgreSQL با استفاده از PostgresHook
•	ذخیره داده در قالب CSV و آپلود در S3
•	اجرای خودکار توسط Airflow DAG به‌صورت روزانه
•	راه‌اندازی آسان با Docker Compose
🚀 نحوه اجرا
۱. کلون کردن مخزن
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
۲. ساخت دایرکتوری‌های موردنیاز
mkdir ./dags ./logs ./plugins
۳. تنظیم متغیرهای محیطی
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
۴. نصب و اجرای Docker Compose
docker-compose up -d
۵. بررسی سرویس‌های در حال اجرا
docker ps
۶. دسترسی به Airflow Webserver
بعد از اجرا، می‌توانید رابط کاربری Airflow را در مرورگر خود باز کنید:
http://localhost:8080
نام کاربری و رمز عبور پیش‌فرض airflow است.
🔗 تنظیمات اتصال در Airflow
برای اتصال PostgreSQL و S3 در Airflow UI:
1.	وارد بخش Admin → Connections شوید.
2.	یک اتصال جدید برای PostgreSQL ایجاد کنید: 
o	شناسه اتصال: postgres_localhost
o	نوع اتصال: Postgres
o	میزبان: postgres
o	پایگاه داده: airflow
o	نام کاربری: airflow
o	رمز عبور: airflow
3.	یک اتصال جدید برای S3 (یا MinIO) ایجاد کنید: 
o	شناسه اتصال: minio_conn
o	نوع اتصال: S3
o	تنظیمات اضافی:
4.	{ "aws_access_key_id": "minio", "aws_secret_access_key": "minio123", "endpoint_url": "http://minio:9000" }
📜 نیازمندی‌ها
apache-airflow
apache-airflow-providers-postgres
apache-airflow-providers-amazon
boto3
نصب وابستگی‌ها:
pip install -r requirements.txt
📂 پایگاه داده نمونه orders.sql))
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    amount NUMERIC,
    date TIMESTAMP
);

INSERT INTO orders (customer_name, amount, date)
VALUES ('Alice', 120.50, '2024-02-10 10:00:00'),
       ('Bob', 75.00, '2024-02-10 12:30:00');




مهدی حسنی
