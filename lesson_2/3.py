import yaml

data = {
    'key1': ['data1', 'data2'],
    'key2': 1,
    'key3': {
        '1U+0024': '1',
        '2U+20BD': '2',
        '3U+0024': '3',
        '4U+0024': '4'
    }

}

with open('file.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=True, allow_unicode=True)

with open('file.yaml') as file:
    file_data = yaml.load(file, Loader=yaml.FullLoader)

if file_data == data:
    print('OK')
else:
    print('Error')

# почему-то у меня не работает вариант с символами в таком виде: ₿, ＄, €, ₽. Пишет UnicodeEncodeError: 'charmap' codec can't encode character '\u20bf' in position 1: character maps to <undefined>