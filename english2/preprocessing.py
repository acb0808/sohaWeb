def main():
    words = []

    with open('convert.txt', 'r', encoding='utf-8') as f:

        # 개행복구 및 변환
        contents = f.read().split('# ')[1:]
        contents = list(map(lambda x : x.split('\n\n'), contents))
        contents = list(map(lambda x : list(map(lambda y : y.lstrip(), x)), contents))


        #파일 무결성 검사
        contents = list(map(lambda x : x if x[0].isdigit() else 1/0, contents))  


        # 전처리 과정
        for chapter in contents:
            chapter = chapter[1:]
            for text in chapter:
                for word in text.split('\n')[1:]:
                    print(word)
                    words.append([word.split('\t')[0], word.split('\t')[1]])

    import json

    with open('words.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(words))

if __name__ == '__main__':
    main()


