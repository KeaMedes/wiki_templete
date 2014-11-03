#coding:utf-8
def set_basic_info():
    method_name = "获取"
    map_url = "/hell"
    request_method = "PUT"
    parameter = [
    {
        "name" : "commId",
        "type" : "Long",
        "required" : "true",
        "passMethod" : "PathVariable",
        "explan" : "管理员要Pass的小区Id"
    },
    {
        "name" : "commId",
        "type" : "Long",
        "required" : "true",
        "passMethod" : "PathVariable",
        "explan" : "管理员要Pass的小区Id"
    }
    ]
    result = [
    {
        "type" : "Code",
        "explan" : None,
        "sample" : None
    },
    {
        "type" : "Json", #could be json, modelandview and code
        "explan" : None,
        "sample" : 
'''
    "obsPlanId": "3FO4K4WI9ALU",
    "linkToFloorPlan": "/huxing/3FO4K4WI9ALU",
    "linkToUser": "/u/null/fplist",
    "planCity": "上海",
    "hasDesign": false,
    "commName": "夏朵小城二期",
    "modifiedTime": 1370319579000,
    "viewCount": 0,
    "cmtCount": 0,
    "pics": "http://qhyxpic.oss.kujiale.com/fpi/2013/06/05/Ua75BkNnRXAW4wFBAAAA.jpeg",
    "area": 104,
    "modelStatus": 0,
    "smallPics": "http://qhyxpic.oss.kujiale.com/fpi/2013/06/05/s_Ua75BkNnRXAW4wFBAAAA.jpeg",
    "isSelfUpload": false,
    "formatModifiedTime": "2013-06-04 12:19",
    "name": "夏朵小城二期104.00㎡A户型2室2厅1卫",
    "provinceId": "0",
    "cityId": "1",
    "planType": "0"
'''
    },
    {
        "type" : "modelandview", #could be json, modelandview and code
        "explan" : [
            {
                "name" : "curpage",
                "exp" : "当前页"
            },
            {
                "name" : "title",
                "exp" : "标题"
            }
        ],
        "sample" : 
'''
    "obsPlanId": "3FO4K4WI9ALU",
    "linkToFloorPlan": "/huxing/3FO4K4WI9ALU",
    "linkToUser": "/u/null/fplist",
    "planCity": "上海",
    "hasDesign": false,
    "commName": "夏朵小城二期",
    "modifiedTime": 1370319579000,
    "viewCount": 0,
    "cmtCount": 0,
    "pics": "http://qhyxpic.oss.kujiale.com/fpi/2013/06/05/Ua75BkNnRXAW4wFBAAAA.jpeg",
    "area": 104,
    "modelStatus": 0,
    "smallPics": "http://qhyxpic.oss.kujiale.com/fpi/2013/06/05/s_Ua75BkNnRXAW4wFBAAAA.jpeg",
    "isSelfUpload": false,
    "formatModifiedTime": "2013-06-04 12:19",
    "name": "夏朵小城二期104.00㎡A户型2室2厅1卫",
    "provinceId": "0",
    "cityId": "1",
    "planType": "0"
'''
    }
    ]
    return (method_name, map_url, request_method, parameter, result)

def gen_templete_basic_part(info):
    return "== %s == \n%s %s" % info

def gen_templete_parameter_part(info):
    def format_parameter(param):
        return "** @%s(value = '%s', required = %s) final %s %s" % (param["passMethod"], param["name"], param["required"], param["type"], param["name"])
    formated_parameter = map(format_parameter, info)
    result = reduce(lambda x, y : x + "\n" + y, formated_parameter, "*入参")
    return result

def gen_templete_parameter_explan_part(info):
    def format_parameter(param):
        return "** %s %s" % (param["name"], param["explan"])
    formated_parameter = map(format_parameter, info)
    result = reduce(lambda x, y : x + "\n" + y, formated_parameter, "*参数解释")
    return result

def gen_result_part_json(info):
    return "** 返回Json \n" + "<pre>\n" + "{\n" + info["sample"] + "}\n" + "<\pre>"

def gen_result_part_modelandview(info):
    exps = map(lambda x : "*** %s : %s"  % (x["name"], x["exp"]), info["explan"])
    exp_part = reduce(lambda x, y : x + "\n" + y, exps, "** 解释:")
    return "** 返回类型: ModelAndView\n" + exp_part + "\n" + "<pre>\n" + "{\n" + info["sample"] + "}\n" + "<\pre>"

def gen_result_part(info):
    def return_type_dispatch(param):
        if (param["type"] == "Code"):
            return "** sucess code 200"
        elif (param["type"] == "Json"):
            return gen_result_part_json(param)
        else:
            return gen_result_part_modelandview(param)

    formated_part = map(return_type_dispatch, info)
    return reduce(lambda x, y : x + "\n" + y, formated_part, "*返回值")
def gen_templete(info):
    basic_part = gen_templete_basic_part((info[0], info[2], info[1]))
    parameter_part = gen_templete_parameter_part(info[3])
    parameter_explan_part = gen_templete_parameter_explan_part(info[3])
    result_part = gen_result_part(info[4])
    all_text = reduce(lambda x , y : x + "\n\n" + y , (basic_part, parameter_part,parameter_explan_part, result_part))
    return all_text

def show_templete(templete):
    print templete

def main():
    basic_info = set_basic_info()
    templete = gen_templete(basic_info)
    show_templete(templete)

if __name__ == '__main__':
    main()