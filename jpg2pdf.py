import argparse
import os
import glob
from PIL import Image
from reportlab.pdfgen import canvas

"""
" 引数処理
" -a : All オプション。現在いるディレクトリ内全てのディレクトリをpdf化する
" Allオプnションがない場合、第一引数のディレクトリを第二引数のpdf名で出力
" 第二引数がないならディレクトリ名がpdfの名前になる
"""
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',nargs='?',default=None, help="jpeg's directory")
    return parser.parse_args()

# all to pdf mode
def convert_all():
    paths= os.listdir(os.getcwd())
    print("before path ",paths)
    print("-------------------")
    for path in paths:
        if os.path.isfile(path):
            paths.remove(path)
            print(path+" is not dir")
            continue
        print(path+" is dir")
    print(paths)

# single to pdf mode
def convert_single(dir_name, pdf_name):
    files = glob.glob(dir_name+'/*.jpg')
    files.extend(glob.glob(dir_name+'/*.PNG'))
    files.extend(glob.glob(dir_name+'/*.jpeg'))
    files.extend(glob.glob(dir_name+'/*.png'))
    # 空要素が入ってたら削除
    if [] in files:
        files.remove([])
    files.sort()

    print("Generate",pdf_name,"\nfrom",dir_name)
    my_canvas = canvas.Canvas(pdf_name)
    for file in files:
        with Image.open(file) as image:
            my_canvas.setPageSize(image.size)
        my_canvas.drawInlineImage(file, 0, 0)
        my_canvas.showPage()

    try:
        my_canvas.save()
    except:
        print("pdf generate error")
    print("Complete")

# mode
# 引数に対応するmodeの関数を返す。convert_single()かconvert_all()を返す
def get_mode():
    args = get_args()
    print(args)
    if args.path is not None:
        dir_name = args.path
        pdf_name = dir_name+".pdf"
        return convert_single(dir_name, pdf_name)
    return convert_all()

# j2p 
if __name__ == '__main__':
    convert = get_mode
    convert()

    
