import sys
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#URL processings
def url_processing(url):

    uid = url.split('/')[3]
    contentid = url.split('/')[-1]
    num1,num2,num3 = cutnumbers(contentid)
    converted_contentid = generate_content_id(num1,num2,num3)
    final_url = generate_pc_url(uid,converted_contentid)

    return final_url

def cutnumbers(num):
    number_string = [str(digit) for digit in str(num)]
    number1 = format_deleting_extra_zero(''.join(str(x) for x in number_string[:2]))
    number2 = format_deleting_extra_zero(''.join(str(x) for x in number_string[2:9]))
    number3 = format_deleting_extra_zero(''.join(str(x) for x in number_string[9:16]))

    return number1,number2,number3

def generate_content_id(num1,num2,num3):
    result1 = encode(num1,BASE62)
    result2 = encode(num2,BASE62).zfill(4)
    result3 = encode(num3,BASE62).zfill(4)
    final_result = result1 + result2 + result3

    return final_result

def format_deleting_extra_zero(num):
    output = int(num)

    return output

def generate_pc_url(uid,contentid):
    finalurl = "https://weibo.com/" + uid + "/" + contentid

    return finalurl

#encoding and decoding functions
def encode(num, alphabet):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for decoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

# url = "https://m.weibo.cn/5901068491/4640077941047684"

url = str(sys.argv[1])
print (url)

processed_url = url_processing(url)
print("变换后URL：" + processed_url)