import wget

num = int(input("enter num to download: "))

url = "https://raw.githubusercontent.com/commaai/calib_challenge/main/labeled/{num}.hevc"

wget.download(url.format(num=num), '{num}.hevc'.format(num=num))


