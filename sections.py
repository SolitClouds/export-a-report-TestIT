# coding: utf8

import api

import re

template = re.compile(r'/api/Attachments/([0-9a-z\-]+)\?*(width=[0-9]+)*\&*(height=[0-9]+)*')
src_template = r'/api/Attachments/[^"]"'


def get_struct(project_id):

    sections = api.get_sections(project_id)
    root = [sec for sec in sections if not sec['parentId']][0]

    def get_tree(parent_id):
        res = [s for s in sections if s['parentId'] == parent_id]
        if res:
            return {s['name']: get_tree(s['id']) for s in res}
        else:
            work_items = [api.get_work_item(w['id']) for w in api.get_section_work_items(parent_id)]
            return [fix_images(w) for w in work_items]

    return get_tree(root['id'])


def fix_images(case):
    for attach in case['attachments']:
        api.load_image("/api/Attachments/" + attach['id'])
    for step in case['steps']:
        step['expected'] = replace_src(step['expected'])
        step['action'] = replace_src(step['action'])
    return case


def replace_src(text):
    res = template.search(text)
    if res:
        if res[1]:
            uuid = res.groups()[0]
            width = res.groups()[1]
            height = res.groups()[2]
            text = re.sub(src_template, '/static/attachments/%s" %s %s'.format(uuid, width, height), text)
        else:
            text = re.sub(src_template, '/static/attachments/%s"' % res.groups()[0], text)

    return text


def tree_to_flat(struct):

    def to_flat(cur_struct, number="1"):

        flat = []

        if type(cur_struct) == dict:
            for k, v in cur_struct.items():

                flat.append({"type": "section", "number": str(number), "name": k})
                if type(v) != str:
                    flat.extend(to_flat(v, number + ".1"))

                l = number.split(".")
                number = '.'.join(l[:-1] + [str(int(l[-1]) + 1)])

        if type(cur_struct) == list:
            for v in cur_struct:
                flat.append({"type": "work_item", "work_item": v})

        return flat

    return to_flat(struct)
