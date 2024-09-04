import os
import pandas as pd

class DataManager:
    # مسیر فایل‌های CSV و Excel
    FILE_PATH_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'students.csv')
    FILE_PATH_XLSX = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'students.xlsx')

    @staticmethod
    def ensure_data_directory_exists():
        """ایجاد پوشه data اگر وجود نداشته باشد."""
        directory = os.path.dirname(DataManager.FILE_PATH_CSV)
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def save_data(students):
        """ذخیره داده‌های دانش‌آموزان در فایل‌های CSV و Excel."""
        DataManager.ensure_data_directory_exists()
        df = pd.DataFrame(students)
        df.to_csv(DataManager.FILE_PATH_CSV, index=False)
        df.to_excel(DataManager.FILE_PATH_XLSX, index=False, engine='openpyxl')  # استفاده از openpyxl برای Excel

    @staticmethod
    def load_data():
        """بارگذاری داده‌های دانش‌آموزان از فایل CSV."""
        if os.path.exists(DataManager.FILE_PATH_CSV):
            return pd.read_csv(DataManager.FILE_PATH_CSV).to_dict(orient='records')
        return []

    @staticmethod
    def delete_student(student_id):
        """حذف یک دانش‌آموز بر اساس شناسه."""
        students = DataManager.load_data()
        updated_students = [student for student in students if student['Student ID'] != student_id]
        DataManager.save_data(updated_students)

    @staticmethod
    def update_student(updated_data):
        """بروزرسانی اطلاعات یک دانش‌آموز."""
        students = DataManager.load_data()
        for i, student in enumerate(students):
            if student['Student ID'] == updated_data['Student ID']:
                students[i] = updated_data
                break
        DataManager.save_data(students)
