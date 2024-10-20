import os
import json

class LatestDirectory:
    @staticmethod
    def process_latest_directory():
        base_directory = "static/Article/Latest"
        articles = []  # قائمة لتخزين مقالات

        # التأكد من وجود المجلد الأساسي
        if os.path.exists(base_directory):
            for folder_name in os.listdir(base_directory):
                folder_path = os.path.join(base_directory, folder_name)
                
                if os.path.isdir(folder_path):
                    article_info = {
                        'id': folder_name,  # يمكن استخدام اسم المجلد كمعرف فريد
                        'title': folder_name,  
                        'description': '',
                        'image_path': '',
                        'article': '',
                        'hashtag':''
                    }

                    files = os.listdir(folder_path)
                    
                    for file_name in files:
                        file_path = os.path.join(folder_path, file_name)
                        
                        if os.path.isfile(file_path):
                            if file_name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                                article_info['image_path'] = file_path  
                            if file_name == 'description.md':
                                with open(file_path, 'r', encoding='utf-8') as file:
                                    article_info['description'] = file.read()  
                            if file_name == 'article.md':
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    article_info['article'] = f.read()
                            if file_name == 'hastic.json':
                                # استخدم المسار الكامل إلى ملف hastic.json داخل folder_path
                                json_file_path = os.path.join(folder_path, file_name)
                                absolute_path = os.path.abspath(json_file_path)
                                print(f"Attempting to open file at: {absolute_path}")

                                with open(json_file_path, 'r', encoding='utf-8') as file:
                                    hashtag_data = json.load(file)  # قراءة ملف JSON وتحويله إلى كائن Python
                                    article_info['hashtag'] = hashtag_data.get('hashtag', [])

                                    # تحقق مما إذا كانت البيانات تحتوي على قائمة داخل قائمة وقم بفكها
                                    
                                    print(article_info['hashtag'])

                    articles.append(article_info)

        return articles
