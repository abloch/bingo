from random import sample
from os import listdir

image_suffixes = ['.jpg', '.jpeg', '.png']
pics = [filename for filename in listdir() if any(filename.lower().endswith(suffix) for suffix in image_suffixes)]

def get_sample(num):
    return sample(pics, num)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def imagize(src):
    return '<img src="../{}" width="600px">'.format(src)

def generate_3_row(chunks):
    (a,b,c)=chunks
    return "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(imagize(a), imagize(b), imagize(c))

def generate_bingo(sample):
    chunks3 = list(chunks(sample, 3))
    rows = [generate_3_row(chunk) for chunk in chunks3]
    table = "".join(rows)
    ret = "<html><head><style></style></head><body><table><tbody>{}</tbody></table></body></html>".format(table)
    return ret

def generate_file(num):
    content = generate_bingo(get_sample(9))
    with open("bingo/{}.html".format(num), "w") as f:
        f.write(content)

for i in range(40):
    generate_file(i)
