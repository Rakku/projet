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
        clazz = my_import(mod, name)  # TODO: Code a method to import a class dynamically
        obj = clazz()
        obj_list.append(obj)
    return obj_list



def load_items(items):
    return load_classes('items.items', items)
    # new_items = []
    # for item in items:
    #     # __import__()
    #     #pass  # TODO: Remove (the pass is here to avoid a Syntax error :))
    #     clazz = my_import('items.' + item)  # TODO: Code a method to import a class dynamically
    #     obj = clazz()
    #     new_items.append(obj)
    # return new_items


def load_skills(skills):
    return load_classes('skills', skills)
        # new_skills = []
        # for skil in skills:
        #     # __import__()
        #     pass  # TODO: Remove (the pass is here to avoid a Syntax error :))
        #     # clazz = my_import('skills.' + item) # TODO: Code a method to import a class dynamically
        #     # obj = clazz()
        #     # new_items.append(obj)
        # return new_skills


# def load_hero_skill(skill_name):
#     return my_import('skills', skill_name)

def load_enemies(enemies):
    return load_classes('enemies', enemies)
    # new_enemies = []
    # for enemy in enemies:
    #     # __import__()
    #     pass  # TODO: Remove (the pass is here to avoid a Syntax error :))
    #     # clazz = my_import('enemies.' + enemy) # TODO: Code a method to import a class dynamically
    #     # obj = clazz()
    #     # new_enemies.append(obj)
    # return new_enemies
