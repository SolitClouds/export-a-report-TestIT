# coding: utf8

#
#   некоторое api от TestIT, необходимое для выгрузки тестовой документации
#

import os
import json
import requests

token = 'PrivateToken ' + os.environ['TOKEN']
baseUrl = os.environ['URL']
url = baseUrl + '/api/v2/'
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": token
}


def get_list_projects():
    res = requests.get(url + "projects?isDeleted=false", headers=headers)
    if res.status_code == 200:
        return {v['id']: v['name'] for v in json.loads(res.text)}
    else:
        raise Exception("not get projects list")


def get_project_work_items(project_id):
    res = requests.get(
        "{url}projects/{project_id}/workItems?isDeleted=false".format(url=url, project_id=project_id),
        headers=headers)
    if res.status_code == 200:
        return [v['id'] for v in json.loads(res.text)][:5]
    else:
        raise Exception("not get workItems in project: %s" % project_id)


def get_work_item(work_item_id):
    res = requests.get("{url}workItems/{id}".format(url=url, id=work_item_id), headers=headers)
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        raise Exception("not load workItem: %s" % work_item_id)


def load_image(image_url):
    res = requests.get("{baseUrl}{imageUrl}".format(baseUrl=baseUrl, imageUrl=image_url))
    if res.status_code == 200:
        with open("./static/attachments/" + image_url[17:], 'wb') as f:
            f.write(res.content)
    else:
        raise Exception("not found image: %s" % image_url)


def get_sections(project_id):
    res = requests.get(
        "{url}projects/{projectId}/sections".format(url=url, projectId=project_id),
        headers=headers
    )
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        raise Exception("not load sections project_id: %s" % project_id)


def get_section_work_items(section_id):
    res = requests.get(
        "{url}sections/{sectionId}/workItems".format(url=url, sectionId=section_id),
        headers=headers
    )
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        raise Exception("not get section's workItems for section_id: %s" % section_id)

