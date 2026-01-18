ssh-copy-id ansible@centos1

# Give ansible passwordless sudo CENTOS
dnf install -y sudo   # or yum install -y sudo
usermod -aG wheel ansible
echo "ansible ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ansible
chmod 440 /etc/sudoers.d/ansible



# oracle db
sqlplus mock_user/mock_password@//oracle:1521/MOCKDB

CREATE TABLE mock_table_1 (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(50)
);

CREATE TABLE mock_table_2 (
    id NUMBER PRIMARY KEY,
    description VARCHAR2(100)
);

CREATE TABLE mock_table_3 (
    id NUMBER PRIMARY KEY,
    created_at DATE
);
SELECT table_name FROM user_tables;
