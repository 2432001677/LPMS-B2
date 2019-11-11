from Project import pymysql
from Project import swim


class DbControl:
    def __init__(self,s):
        #conn = pymysql.connect (host = "cdb-pllfd5fy.bj.tencentcdb.com", port = 10146, user = "root", passwd = "wangsong990315", db = "lpms",charset="utf8")
        self.swim=s

    def select(self,sql):
        # conn = pymysql.connect(**self.dbConfigure)
        conn = pymysql.connect(host="cdb-pllfd5fy.bj.tencentcdb.com", port=10146, user="root", passwd="wangsong990315",
                               db="lpms", charset="utf8")

        cur = conn.cursor()
        cur.execute(sql)

        result = cur.fetchall()
        conn.commit()
        return result
        print(result)

    def insert(self):
        # conn = pymysql.connect(**self.dbConfigure)
        conn = pymysql.connect(host="cdb-pllfd5fy.bj.tencentcdb.com", port=10146, user="root", passwd="wangsong990315",
                               db="lpms", charset="utf8")

        cur = conn.cursor()
        ids=self.select("select max(id) from swimdata")
        id=str(ids[0][0]+1)
        swim_name=self.swim.name
        swim_time=str(self.swim.all_time)
        swim_distance=str(self.swim.sum_distance)
        swim_number=str(self.swim.number)
        swim_oncetime=str(self.swim.once_time)
        swim_avergepace=str(self.swim.averagepace)
        swim_maxpace=str(self.swim.maxpace)
        swim_avergerate=str(self.swim.averagerate)
        swim_maxrate=str(self.swim.maxrate)
        swim_date=str(self.swim.date)
        fp = open("WinUI/mat.png", 'rb')
        img = fp.read()
        fp.close()
        swim_pace_pic=str(img)
        swim_rate_pic=str(img)
        sql = "insert into swimdata (" \
              "id,swim_name,swim_time,swim_distance," \
              "swim_number,swim_oncetime,swim_avergepace," \
              "swim_maxpace,swim_avergerate,swim_maxrate," \
              "swim_date) " \
              "value ('"+id+"','"+swim_name+"','"+swim_time+"','"+swim_distance+"','"+swim_number+"','"+swim_oncetime+ "','" +swim_avergepace+"','"+swim_maxpace+"','"+swim_avergerate+ "','" +swim_maxrate+"','"+swim_date+"');"
        #
        # args = (id,swim_name,swim_time,swim_distance,
        #         swim_number,swim_oncetime,swim_avergepace,
        #         swim_maxpace,swim_avergerate,swim_maxrate,
        #         swim_date,swim_pace_pic,swim_rate_pic)

        cur.execute(sql)
        conn.commit()
        result = cur.fetchall()


if __name__ == '__main__':
    y=[2]
    s=swim.Swim(y)
    eee = DbControl(s)
    id=eee.select("select max(id) from swimdata")
    print(id[0][0]+1)
