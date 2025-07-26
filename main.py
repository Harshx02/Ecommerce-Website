with open("D:\\test\\test\\ProductCatlog-master\\ChazeFashion\\templates\\catalog\\product_list.html", "r", encoding="ISO-8859-1") as f:
    lines = [line.lstrip("+") for line in f]

with open("D:\\test\\test\\ProductCatlog-master\\ChazeFashion\\templates\\catalog\\product_list.html", "w", encoding="ISO-8859-1") as f:
    f.writelines(lines)
