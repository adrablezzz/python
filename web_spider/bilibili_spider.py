import sys
import you_get

def download(url, path):
    # '--format=dash-flv'
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()

if __name__ == '__main__':
    # 要下载的视频地址
    # url = 'https://www.bilibili.com/video/BV1mD4y1U7z9/'
    url = 'https://v.qq.com/x/cover/31082i4u5ovkrl0/s00211yt19u.html'
    # url = 'https://v.qq.com/x/cover/mzc00200vvfld1j/m00135c6uxe.html'
    # 视频保存的位置
    path = r'D:\Downloads'

def parser(url):
    sys.argv = ['you-get', '-i', url]
    you_get.main()

# parser(url)
download(url, path)