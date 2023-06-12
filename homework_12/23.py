import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.readlines()

    new_list = []
    for item in html:
        item = item.replace("\n", "")
        new_list.append(item)

    join_text = "".join(new_list)
    cleaned_text = re.sub(r'<.*?>', '', join_text)

    cleaned_text = '\n'.join(line for line in cleaned_text.splitlines() if line.strip())

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)


delete_html_tags("draft.html")
