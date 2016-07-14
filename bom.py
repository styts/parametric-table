def print_bom(items):
    print "/****************************"
    print "      Bill of Materials"
    print "****************************"
    for count, cls in items:
        total_length = count * cls.length
        # max_length = cls.lumber.length * buying[cls.lumber.__name__]
        max_length = cls.lumber.length
        rest = max_length - total_length
        print cls.__name__, "[x%s]" % count, "\n-----------------------------"
        # print calculate_max(buying, items)
        print "Lumber:", cls.lumber.__name__, cls.lumber.print_name()
        print "Single length:", cls.length
        print "Total length:", total_length
        print "Max length:", max_length
        print "Used:", total_length / float(max_length) * 100.0, "%"
        print "Allowed:", total_length <= max_length
        print "Rest:", rest, "\n"

        """
        print "****************************"
        print "      Shopping List "
        print "****************************"
        for lumber_name, data in buying.iteritems():
            print lumber_name, data
        """
    print "****************************/"
