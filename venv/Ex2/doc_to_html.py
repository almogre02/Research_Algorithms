'''
כתבו תוכנית, המקבלת כקלט שם של קובץ פייתון המכיל מודול מסויים, ושם של קובץ פלט, ויוצרת קובץ HTML המתעד
את המודול: שמות הפונקציות שיש במודל, והתיעוד של כל פונקציה.
'''

import importlib


def get_doc(module_name,output_file):
    #index = module_name.find('.py')
    #module = module_name.removesuffix('.py')
    module=module_name[:-3]
    module = importlib.import_module(module)
    print (module.__name__)
    func_names=module.__dir__()[8:]
    print(func_names)
    with open(output_file,'w') as file:
        file.write("<html>\n<head>\n<title>\n \
                    </title>\n</head> <body><h1>"
                    )
        file.write(str(module.__name__) + "\n")
        file.write(str(module.__doc__) +"\n")
        for func in func_names: #get the documentation & annotation from every func in the module
            attr=getattr(module,func) #getattr = get the value of an object’s attribute
            func_doc=attr.__doc__
            func_ano=attr.__annotations__
            if func_doc is None:
                func_doc="There isn't documentation for this function"
            file.write("\n"+f"Function:{func},documentation: {func_doc}, annotations: {func_ano} "+"\n")
            print(f'Function {func},documentation: {func_doc}, annotations: {func_ano}')
        file.write("</h1>\n \
                       </body></html>")
        file.close()


if __name__ == '__main__':
    get_doc("mymodule.py","mydoc.html")