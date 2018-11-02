# -*-coding:utf-8-*-
import time
import json
import requests
import traceback
import urllib2
import schedule


# alert time
def post_to_weixin(msg="default", Secret="m", AppID=100,
                   CropID="ww497dd961480bfc5a"):
    try:
        PartyID = 1
        GURL = "" % (CropID, Secret)
        result = urllib2.urlopen(urllib2.Request(GURL)).read()
        dict_result = json.loads(result)
        Gtoken = dict_result['access_token']

        PURL = "" % Gtoken
        post_data = {}
        msg_content = {}
        msg_content['content'] = msg
        # post_data['touser'] = 0
        post_data['toparty'] = 1
        # post_data['touser'] = "xxx"
        post_data['msgtype'] = 'text'
        post_data['agentid'] = AppID
        post_data['text'] = msg_content
        post_data['safe'] = '0'

        json_post_data = json.dumps(post_data, ensure_ascii=False).encode('UTF-8')
        print json_post_data
        request_post = urllib2.urlopen(PURL, json_post_data)
        print(request_post)
        return request_post.read()
    except Exception:
        print traceback.format_exc()


###############################################
def dingding_alert(content):
    url = ""
    header = {
        "Content-Type": "application/json",
        "charset": "utf-8"
    }

    data = {

        "msgtype": "text",
        "text": {
            "content": content

        },
        "at": {
            "isAtAll": "false"

        }
    }
    sendData = json.dumps(data)
    request = urllib2.Request(url, data=sendData, headers=header)
    urlopen = urllib2.urlopen(request)
    print urlopen.read()


#################################################
# time container
url_31 = "http:"
url_21 = "http:"
url_O31 = "http:"
url_O21 = "http:"

time_data = [url_31, url_21, url_O31, url_O21]


def get_now_res(url):
    re = requests.get(url)
    print "result data@!!!!"
    return re.text


def judge(datas):
    print "judge datas"
    print datas
    print datas[-1]
    print datas.split()[0]
    print datas.split()[1]
    print datas.split()[-2][:4]
    print datas.split()[-2][-4:]
    print "judge ok"
    if datas[-1] == ";" or datas.split()[0] == "var" or datas.split()[1] == "now" or datas.split()[-2][:4] == "Date" or datas.split()[-2][-4:] == "2018":
        return "1"
    else:
        return "0"


def clean_data():
    for da in time_data:
	     res = get_now_res(da)
            datas = res.encode("utf-8")
            print "-------------------------------"
            print datas
            result = judge(datas)
            print "result      "
            print result
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if result  and result == "1":
                pass
                # post_to_weixin("Current time:\n{0};\nTime container is {1},\nthe url is:\n{2}\n".format(cur_time,"time", da))
            if result and result == "0":
                dingding_alert(
                    "Current time:\n{0};\nTime container is {1},\nIt has trackface;\nplease attention!!\n erro_body{2};\nresult:{3}\nthe Api is:\n{4}\n".format(
                        cur_time, "time",datas,result ,da))
  #      try:
       
   #     except Exception:
   #         cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   #         dingding_alert(
   #            "Current time:\n{0};\nTime container is {1},\nIt has trackface:\n{2};\nplease attention!!\n{3}\nthe Api is:\n{4}\n".format(
   #                 cur_time, "time",json.dumps(traceback.format_exc()),datas ,da))

            # con_one = datas[-1] # ;
            # con_two = datas.split()[0] # var
            # con_thr = datas.split()[1] # now
            # con_for = datas.split()[2] # =
            # con_fiv = datas.split()[3] # new
            # con_six = datas.split()[-2][:4] # Date
            # con_seven = datas.split()[-2][-4:] # 2018


api_url_33 = "http:"
api_url_34 = "http:"
api_url_35 = "http:"
api_url_36 = "http:"


def clean_api_web():
    data = [api_url_33, api_url_34, api_url_35, api_url_36]
    for da in data:
        try:
            res = get_now_res(da)
            haha = json.loads(res)
    #        print haha, type(haha)
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if haha.has_key("serverTime") or haha.has_key("videoList") or haha.has_key("total"):
                pass
                # post_to_weixin("Current time:\n{0};\nweb-api container is test,\nplease attention!!\nAPI:{1}".format(cur_time,da))
            else:
                dingding_alert(
                    "Current time:\n{0};\nweb-api container has traceback,\nplease attention!!\nAPI:{1}".format(cur_time,
                                                                                                                da))
        except Exception:
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            dingding_alert(
                "Current time:\n{0};\nweb-api container has traceback:{1},\nplease attention!!\nAPI:{2}".format(cur_time,json.dumps(traceback.format_exc()),
                                                                                                            da))



def keep_alive():
    print "123"
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dingding_alert("Current time:\n{0};\nThis is keep_alivet!!\nFrequency (every 60 min) ~(*=.=*)~!!!!".format(cur_time))

if __name__ == '__main__':
    keep_alive()
    schedule.every(5).minutes.do(clean_data)
    schedule.every(5).minutes.do(clean_api_web)
    schedule.every(180).minutes.do(keep_alive)
    while True:
        schedule.run_pending()
        time.sleep(1)