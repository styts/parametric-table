def print_bom(items, buying):
    print "/****************************"
    for count, cls in items:
        total_length = count * cls.length
        max_length = cls.lumber.length * buying[cls.lumber.__name__]
        rest = max_length - total_length
        print cls.__name__, "[x%s]" % count, "\n---------------------"
        print "Lumber:", cls.lumber.__name__, cls.lumber.print_name()
        print "Single length:", cls.length
        print "Total length:", total_length
        print "Max length:", max_length
        print "Used:", total_length / float(max_length) * 100.0, "%"
        print "Allowed:", total_length <= max_length
        print "Rest:", rest, "\n"

    print "****************************/"
