# vega_mysql
MySQL를 사용하기 위한 라이브러리

    * 의존성:
        - python 3.8.10 이상
        - PyMySQL 1.0.2 이상
        - sshtunnel 0.4.0 이상

------------------
### 사용법
```
    # install
        $  pip install git+ssh://git@github.com/jinland-bommaru/vega_mysql.git

    # chromedriver 사용 시
        from vega_mysql import MySQL, MySQLError
                :
                :
        mysql = MySQL(
            host="ip-address or dns",
            port=port number,
            user="connect user id",
            passwd="user passwd",
            database="database name"
            charset="utf8'
                :
        )
                :
        # mysql 접속
        conn = mysql.connect()
                :
        # mysql 접속 해제
        mysql.disconnect()

    [참고]
    conn = mysql.connect()를 통해서 mysql driver를 획득했을 경우 driver는 PyMySQL의 모든 메소드를 사용할 수 있다.

```

------------------
### ARG 정의
```
    # tunneling
        - 형식: Boolean
        - 설명: mysql 접속을 tunneling을 통해 할 것인가 선택. 기본값 False
    # host
        - 형식: string
        - 설명: database가 위한한 서버의 ip-addr 또는 DNS로 필수입력값
    # port
        - 형식: int
        - 설명: database port. 기본값 3306
    # user
        - 형식: string
        - 설명: database user id. 필수입력값
    # passwd
        - 형식: string
        - 설명: database user password. 필수입력값
    # database
        - 형식: string
        - 설명: 데이타베이스명. 필수 입력값
    # charset
        - 형식: string
        - 설명: database의 글자 형식 지정. 기본값 utf8
    # ssh_host
        - 형식: string
        - 설명: ssh tunneling을 위한 서버 ip-addr 또는 DNS. tunneling이 True이면 필수 입력값
    # ssh_port
        - 형식: int
        - 설명: ssh tunneling을 위한 포토번호. 기본값 22
    # ssh_user
        - 형식: string
        - 설명: tunneling 접속을 위한 사용자 아이디.
    # ssh_passwd
        - 형식: string
        - 설명: tunneling user의 비밀번호
    # ssh_key
        - 형식: string
        - 설명: 공개키를 사용한다면 그 키의 경로
    [주의]
        tunneling 시 ssh_passwd와 ssh_key값은 하나만 존재해야 한다.
```

------------------
### method 정의
```
    # connect()
      database에 접속을 위한 메소드
    # close()
      database 접속 해제를 위한 메소드
```