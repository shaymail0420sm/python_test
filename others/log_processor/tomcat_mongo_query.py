# encoding:utf-8

def read_log():
    fh = open('catalina.out')
    content = []
    counter = 0
    for l in fh:
        # print l
        if '[com.luyouchina.train.core.common.util.ModuleUtils#callService:66]' in l:
            content.append(process_line(l))
            counter += 1
    print counter

    write_to_sql('\n'.join(content))

def process_line(line):
    a = line.index('执行')
    b = line.index('成功')

    c = line.index('耗时')

    d = line.index('参数')
    x = len('参数')
    log_time = line[:19]
    module_method = line[a+x:b]
    spend = line[c+x:d].replace('ms，', '')
    param = line[d+x:-2]
    mysql_format = 'insert into mongo_query(module_method, spend, param, log_time) values (\'%s\', %s, \'%s\', \'%s\');'
    print log_time
    return mysql_format % (module_method.strip(), spend.strip(), param.strip()[:-1], log_time)


def write_to_sql(content):
    fh = open('log.sql', 'w')
    fh.write(content)
    fh.close()


if __name__ == '__main__':
    read_log()