__author__ = 'Kazesoushi'

# COMPLETE

def my_import(mod, class_name):
    mod = __import__(mod, fromlist=[class_name])
    components = class_name.split('.')
    for comp in components:
        # print 3
        # print mod.__name__
        # print comp
        try:
            mod = getattr(mod, comp)
        except:
            mod = None
        # print "LOOP"
    # print mod
    return mod


def load_classes(mod, name_list):
    obj_list = []
    for name in name_list:
        # c = '%s.%s.%s' % (mod, mod, name)
        # print c
        clazz = my_import(mod, name)
        obj = clazz()
        obj_list.append(obj)
    return obj_list


def load_items(items):
    return load_classes('items.items', items)


def load_skills(skills):
    return load_classes('skills', skills)


def load_enemies(enemies):
    return load_classes('enemies', enemies)
