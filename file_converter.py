class Converter:
    def __init__(self, filename, headers, csv_filename):
        self.filename = filename
        self.headers = headers.strip().split(' ')
        self.csv_filename = csv_filename
        self.__convert_json_2_csv__()

    @staticmethod
    def __get_method__(obj, method_name='__getitem__', param=''):
        try:
            return getattr(obj, method_name)(param)
        except KeyError:
            return None

    def __write_csv__(self, content):
        import csv
        with open(self.csv_filename, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(self.headers)
            for line in content:
                writer.writerow(line)

    def __convert_json_2_csv__(self):
        import json
        all_rows = list()
        with open(self.filename, "r") as inFile:
            for i, line in enumerate(inFile):
                each_row = list()
                tweet = json.loads(line)
                for each_header in self.headers:
                    if '.' not in each_header:
                        each_row.append(self.__get_method__(tweet, param=each_header))
                    else:
                        _tweet_cache = tweet
                        for each_key in each_header.split('.'):
                            _tweet_cache = self.__get_method__(_tweet_cache, param=each_key)
                            if _tweet_cache is None:
                                break
                        each_row.append(_tweet_cache)
                all_rows.append(each_row)


if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    Converter(config['DEFAULT']['filename'],
              config['DEFAULT']['headers'],
              config['DEFAULT']['csv_filename'])
