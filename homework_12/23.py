import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        print(html)

    cleaned_text = re.sub(r'<.*?>', '', html)  # Видалення html-тегів

    # Видалення рядків без інформації
    cleaned_text = '\n'.join(line for line in cleaned_text.splitlines() if line.strip())

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

delete_html_tags("draft.html")
