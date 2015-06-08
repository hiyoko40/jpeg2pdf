import argparse
import os

"""
" 引数処理
" -a : All オプション。現在いるディレクトリ内全てのディレクトリをpdf化する
" Allオプnションがない場合、第一引数のディレクトリを第二引数のpdf名で出力
" 第二引数がないならディレクトリ名がpdfの名前になる
"""
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--all',help="all directory mode",action='store_true')
    parser.add_argument('path',nargs="+")
    return parser.parse_args()

# all to pdf mode
def convert_all():
    print("all to pdf mode")

# single to pdf mode
def convert_single(dir_name, pdf_name):
    print(dir_name+" to "+pdf_name+" pdf mode")
    
print(os.listdir(os.getcwd()))

# mode
# 引数に対応するmodeの関数を返す。convert_single()かconvert_all()を返す
def get_mode():
    args = get_args()
    if args.all :return convert_all
    dir_name = args.path[0]
    # 第二引数がないなら、directory名をpdf名にする
    pdf_name = args.path[1] if len(args.path)>2 else dir_name+".pdf"
    return convert_single(dir_name, pdf_name)

# j2p 
if __name__ == '__main__':
    convert = get_mode
    convert()

    
