from datetime import datetime
from pyoko.field import DATE_FORMAT

__author__ = 'Evren Esat Ozkan'
from pyoko.form import ModelForm, Form

class AngularForm(Form):
    def serialize(self):
        result = {
            "schema": {
                "title": self.title,
                "type": "object",
                "properties": {},
                "required": []
            },
            "form": [],
            "model": {}
        }
        listnode = {"type": "fieldset", "items": []}
        listnodename = ""
        for itm in self._serialize():
            if isinstance(itm['value'], datetime):
                itm['value'] = itm['value'].strftime(DATE_FORMAT)
            result["schema"]["properties"][itm['name']] = {'type': itm['type'],
                                                           'title': itm['title']}
            result["model"][itm['name']] = itm['value'] or itm['default']

            if itm["storage"] == "ListNode":
                if listnodename == "":
                    listnodename = itm["section"]
                    listnode["name"] = listnodename
                if listnodename == itm["section"]:
                    listnode["items"].append({"key": itm['name'], "title": itm['title']})
                else:
                    result["form"].append(listnode)
                    listnode = {"type": "fieldset", "items": [], "name": itm["section"]}
                    listnode["items"].append({"key": itm['name'], "title": itm['title']})
                    listnodename = itm["section"]
            else:
                result["form"].append(itm['name'])
            if itm['required']:
                result["schema"]["required"].append(itm['name'])
        result["form"].append(listnode)
        return result


