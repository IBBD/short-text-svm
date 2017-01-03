# -*- coding: utf-8 -*-
#
# Author: Alex
# Created Time: 2016年12月28日 星期三 16时42分24秒

import re
from numpy import mean, median

re_patterns = {}

patterns = {
    "zhandao": u"摆地摊|摆摊|占道|占用车道|占用道路|乱摆乱卖|乱摆卖",
    "daolu": u"交通拥堵|非常拥堵|红绿灯坏了|没有路灯|公交线路|公交车|城巴|修路|人行天桥|塞车|路灯坏了|路灯已坏|红绿灯已坏|泥头车|占用机动车道|交通问题|交通堵塞|新能源汽车|免费乘车|造成.{0,6}拥堵|超速|醉驾|酒驾",
    "huanjing": u"环境污染|PM2.5|臭味|空气污染|光污染|辐射污染|毒气|有毒气体|有毒的气体|环保部门|废气|恶臭|下水道|卫生环境|油烟|雾霾|污染|破坏环境|焚烧垃圾|乱排污|臭气薰天|脏乱差",
    "gonggong": u"公共区域|公园厕所|公共厕所|公共设施",
    "tingche": u"停车收费|乱停车|违章停车|停车费|占道停车|非法停车|乱停乱放",
    "weigui": u"违建|违规加建|违规建筑|违法建筑|违规施工|违规建设|违法建房",
    "zaoyin": u"噪音|噪声|无法入睡|噪声污染",
    "shipin": u"食品安全|过期食品|不安全食品|伪劣食品|假冒食品|食品过期|无生产日期|不卫生食品|问题奶粉",
    "jiaoyu": u"无法上学|积分入学|中小学|上学|小孩入读|培训补贴",
    "yiliao": u"医疗|计生办",
    "zhufang": u"房产证|房产无法入户|房产过户|二手房|物业管理|房管所|住房补贴|住房过户|住房公积金|住房困难|住房补贴|旧房改造|宅基地",
    "laodong": u"扣工资|拖欠工资|离职工资|工资标准|最低工资|加班费|双倍工资|发工资|苛扣工资|劳动法|劳动局|劳动合同|劳动部门|劳动监察|劳动报酬|缴纳住房公积金|养老金|就业补贴",
    "xiaotou": u"小偷|治安|被盗",
    "jiakao": u"驾考|驾照考试|驾照约考|考.{0,5}驾照|驾校",
    "xiaofei": u"退货|退钱|退款|退还定金|不打表|出租车拼客|退还货款|退订金|霸王条款|欺诈消费者|欺詐消費者|欺诈销售|强买强卖",
    "wangluo": u"电信.{0,3}收费",
    "zhengfu": u"政府服务|车辆注销|轻轨施工|会计证|港澳通行证|户籍迁移|转户口|迁户口|入户|高级职称|职称评定|居住证.{0,3}办理|初级职称|中级职称|从业资格证|补办.{0,3}身份证"
}

for key in patterns:
    re_patterns[key] = re.compile(r"(%s)" % patterns[key])


def findSecondVal(data, notKey):
    """
    找到字典中除了某个key之外的最大值
    """
    val = 0
    ret_key = ""
    for key in data:
        if data[key] > val and key != notKey:
            val = data[key]
            ret_key = key

    return ret_key, val


def statOutput(title, data):
    print("\n%s: count: %d, max: %f, min: %f, mean: %f, median: %f" %
          (title, len(data), max(data), min(data), mean(data), median(data)))
