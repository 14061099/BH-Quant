echo """#!/usr/bin/expect -f
# 设置ssh连接的用户名
set user hadoop
# 设置ssh连接的host地址
set host 219.224.169.45
# 设置ssh连接的port端口号
set port 6023
# 设置ssh连接的登录密码
set password buaascse
# 设置ssh连接的超时时间
set timeout -1

spawn ssh \$user@\$host -p \$port
expect \"*password:\"
# 提交密码
send \"\$password\\r\"
# 控制权移交
interact
"""   >> Login.sh

chmod 777 Login.sh

