# vega-lib
### Dependancy
```
    'PyMySQL >= 1.0.2',
    'sshtunnel >= 0.4.0',
    'pytz >= 2021.3',
    'python-dateutil >= 2.8.2',
    'psutil >= 5.8.0',
    'slack-sdk >= 3.11.2',
    'beautifulsoup4 >= 4.10.0',
    'selenium >= 4.0.0'
```


### Install
```
    # Download and install with git clone
        $ git clone https://github.com/jinland67/vega-lib.git
        $ cd vega-lib
        $ python setup.py install

    # Installing directly with pip
        $ pip install git+https://github.com/jinland67/vega-lib.git
```

### Usagae
- mysql
```
    # Non tunneling connect
        from vega.database.mysql import MySQL, MySQLError
                    :
                    :
        mysql = MySQL(
            host="ip-address or dns",
            port=port number [default 3306],
            user="connect user id",
            passwd="user passwd",
            database="database name"
            charset="database character set [default utf8]'
                :
        )
                :
        # mysql connect
        conn = mysql.connect()
                :
        # mysql close connect
        mysql.close()

    # Tunneling connect with ssh key
        from vega.database.mysql import MySQL, MySQLError
                        :
                        :
        mysql = MySQL(
            ssh_host="tunneling ip or dns",
            ssh_port="tunneling port [default 22]",
            ssh_key="~/.ssh/<key-file>.pem",
            host="ip-address or dns",
            port=port number [default 3306],
            user="connect user id",
            passwd="user passwd",
            database="database name"
            charset="database character set [default utf8]'
        )

    # Tunneling connect with ssh user password
        from vega.database.mysql import MySQL, MySQLError
                        :
                        :
        mysql = MySQL(
            ssh_host="tunneling ip or dns",
            ssh_port="tunneling port [default 22]",
            ssh_="ssh user password",
            host="ip-address or dns",
            port=port number [default 3306],
            user="connect user id",
            passwd="user passwd",
            database="database name"
            charset="database character set [default utf8]'
        )

    # connect & close to database
        # connect
        conn = mysql.connect()
                :
        # close
        mysql.close()

    # example
        conn = mysql.connect()
        query = " SELECT * FROM sample_table; "
        result = mysql.fetchone(query)
        print(result)
        mysql.close()
```

- web_driver
```
    # connect_type
        - "grid-hub"
        - "chromedriver"

    # When using chromedriver
        from vega.web_driver.selenium import WebDriver, WebDriverError
                :
                :
        browser = WebDriver(
            "connect_type",
            driver_path="chromedriver "./driver/chromedriver",
                :
        )
                :
        driver = browser.connect()
        if driver is not None:
            browser.get(url)
                :
                :
        browser.disconnect() or browser.quit()

    # When using selenium grid hub
        from vega.web_driver.selenium import WebDriver, WebDriverError
                :
                :
        browser = WebDriver(
            "connect_type",
            session_url="<ip-address or dns>:4444"
        )
                :
                :
        driver = browser.connect()
        if driver is not None:
            browser.get(url)
                :
                :
        browser.disconnect() or browser.quit()

    # request selenium web driver
    driver = browser.get_driver()

    # request page from web site
    browser.get(url)

    # request page source
    html = browser.page_source()
```

- utils
```
    # When using file logger
        from vega.utils.logger import FileLogger, FileLoggerError, LogLevel
                :
                :
        log = FileLogger(
            log_path="./log/",
            log_file="test.log",
            log_level = LogLevel.DEBUG,
            log_compress=True
        )
                :
        # log write
        log.debug('this is a test log. time[%s]', time.time())
                :
    # When using socket logger
        from vega.utils.logger import SocketLogger, SocketLoggerError, LogLevel
                :
                :
        log = SocketLogger(
            log_host="localhost",
            log_port=5000,
            log_level = LogLevel.DEBUG
            service_name='stree'
        )
                :
        # log write
        log.debug('this is a test log. time[%s]', time.time())

    # When using ProcessHandle
        from vega.utils.process import ProcessHandle as ph
                :
                :
        result = ph.pids()

    # When using NetworkHandle
        from vega.utils.network import NetworkHandle as nh
                :
                :
        result = nh.is_url()

    # When using StringHandle
        from vega_utils.string import StringHandle as sh
                :
                :
        result = sh.emoji(value)

    # When using DateHandle
        from vega_utils.datetime import DateHandle as dh
                :
                :
        result = dh.now()

    # When using message send with Slack
        from vega_utils.slack import Slack as slack
                :
                :
        slack.send('slac webhook url', blocks)
        # Sends the message format to be sent in blocks. See the slack website for the format.
```