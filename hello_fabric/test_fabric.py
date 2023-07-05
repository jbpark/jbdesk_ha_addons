from fab import get_os_version, get_os_version_without_gateway

if __name__ == '__main__':
    passwords = {}
    passwords["192.168.0.10"] = "passwd"
    os_version = get_os_version("192.168.0.1", "192.168.0.10", "user", "passwd", passwords)
    print("os version:%s" % os_version)

    #os_version = get_os_version_without_gateway("192.168.0.10", "user", "passwd")
    #print("os version:%s" % os_version)
