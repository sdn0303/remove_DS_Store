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


if __name__ == "__main__":
    """ ディレクトリ内に
    .DS_Storeが存在したら削除する。
    """
    for file_path in file_iterator(root_dir='.'):
        if ".DS_Store" in file_path:
            os.remove(file_path)
            print('{} was deleted.'.format(file_path))
    print('Directory is clean.')
