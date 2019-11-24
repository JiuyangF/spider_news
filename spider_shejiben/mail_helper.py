import datetime
import smtplib
from email.mime.text import MIMEText


class MyEmail:
    def send(self, message, to_user):
        try:
            user = "shejiben_sunfuss@163.com"
            passwd = "a1b2c3d4"
            server = smtplib.SMTP("smtp.163.com", 25)
            server.login(user, passwd)
            server.sendmail("<%s>" % user, to_user, self.get_attach(message))
            server.quit()
            print("send email successful")
        except Exception as e:
            print("send email failed %s" % e)

    def get_attach(self, message):
        html = """
        <html>
          <head></head>
          <body>
            <p>
               {}
            </p>
          </body>
        </html>
        """.format(message)
        # Record the MIME types of both parts - text/plain and text/html.
        # part2 = MIMEText(html, 'html')
        #         message = """
        # {},
        # 标题：{},
        # 价格：{},
        #         """.format(url, title, price).encode('utf-8')
        attach = MIMEText(html, 'html', 'utf-8')
        attach["Subject"] = "设计任务 {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        attach["From"] = "发件人<shejiben_sunfuss@163.com>"
        return attach.as_string()


if __name__ == '__main__':
    # MyEmail().send("978","lill@knowbox.cn")
    MyEmail().send("6783", ["yangjt@knowbox.cn"])
    # MyEmail().send("37834", ["1635375337@qq.com"])
