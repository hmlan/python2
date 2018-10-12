def print_case(*args):
    case_number,case_name=args
    print("用例编号:",case_number)
    print("用例名称:",case_name)
    def print_delimiter(delimiter):
        print(delimiter*20)
    def print_end():
        print("打印结束")
    print_case("001",'验证get请求的返回状态码')
    print_delimiter("*")
    print_case("002", '验证get请求的返回返回值')
    print_delimiter("*")
    print_end()
         