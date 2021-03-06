# -*- coding: utf-8 -*-
import os


def file_iterator(root_dir: str) -> str:
    """ ディレクトリ巡回して
    ファイルパス一覧を取得
    """
    for path, dirs, files in os.walk(root_dir):
        yield path
        for file in files:
            yield os.path.join(path, file)

            
def main():
    return (file_path for file_path in file_iterator(root_dir='.') if ".DS_Store" in file_path)

if __name__ == "__main__":
    """ ディレクトリ内に
    .DS_Storeが存在したら削除する。
    """

    for f in main():
        os.remove(f)
        print('{} was deleted.'.format(f))
    print('Directory is clean.')
