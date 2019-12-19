import suanpan
from suanpan.app import app
from suanpan.app.arguments import Folder,File
import os

@app.input(Folder(key="inputData1"))
@app.output(Folder(key="outputData1"))
def pdf2word(context):
    args = context.args
    print("*"*20)
    print(args.inputData1)
    folder = args.inputData1 + "/" + os.listdir(args.inputData1)[0]
    f_list = os.listdir(folder)
    for f in f_list:
        f_name = folder + "/" + f
        res_name = "res/" + f.replace(".pdf",".doc")
        os.system("abiword --to=doc --to-name=%s %s"%(res_name,f_name))


    return "res"


if __name__ == "__main__":
    suanpan.run(app)
