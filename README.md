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
            charset="utf8'
                :
        )
                :
        # mysql connect
        conn = mysql.connect()
                :
        # mysql close connect
        mysql.disconnect()

    # Tunneling connect with ssh key
        from vega.database.mysql import MySQL, MySQLError
                        :
                        :
        mysql = MySQL(
            ssh_host="tunneling ip or dns",
            ssh_port="tunneling port [default 22]",
            ssh_key="~/.ssh/<key-file>.pem",
            host="ip-address or dns",
            port=port number,
            user="connect user id",
            passwd="user passwd",
            database="database name"
            charset="utf8'
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
            port=port number,
            user="connect user id",
            passwd="user passwd",
            database="database name"
            charset="utf8'
        )
```

