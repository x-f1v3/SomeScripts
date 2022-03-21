from PIL import Image
import os


"""不改变图片尺寸压缩到指定大小        
:param infile: 压缩源文件        
:param outfile: 压缩文件保存地址        
:param mb: 压缩目标，KB        
:param step: 每次调整的压缩比率        
:param quality: 初始压缩比率        
:return: 压缩文件地址，压缩文件大小    
"""  

def compress_image(infile, outfile='', mb=1024, step=20, quality=95):
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir_, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir_, suffix)
    return outfile


def get_size(file):
    size = os.path.getsize(file)
    return size / 1024

if __name__ == '__main__': 
    compress_image(r'/xxx/1.jpg')








