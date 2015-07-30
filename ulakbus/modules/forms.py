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
            "model": {},
            "nodes": [],
            "listnodes": []
        }
        node = {"type": "fieldset", "items": []}
        nodename = ""
        for itm in self._serialize():
            if isinstance(itm['value'], datetime):
                itm['value'] = itm['value'].strftime(DATE_FORMAT)
            result["schema"]["properties"][itm['name']] = {'type': itm['type'],
                                                           'title': itm['title']}
            result["model"][itm['name']] = itm['value'] or itm['default']
            # if model includes node or listnode
            if itm["storage"] in ["ListNode", "Node"]:
                if nodename == "":
                    nodename = itm["section"]
                    node["title"] = nodename
                    result["nodes"].append(itm["section"]) if itm["storage"] is "Node" else result["listnodes"].append(itm["section"])
                if nodename == itm["section"]:
                    node["items"].append({"key": itm['name'], "title": itm['title']})
                else:
                    result["form"].append(node)
                    result["nodes"].append(itm["section"]) if itm["storage"] is "Node" else result["listnodes"].append(itm["section"])
                    node = {"type": "fieldset", "items": [], "title": itm["section"]}
                    node["items"].append({"key": itm['name'], "title": itm['title']})
                    nodename = itm["section"]
            else:
                result["form"].append(itm['name'])
            if itm['required']:
                result["schema"]["required"].append(itm['name'])
        # last node stays not added so add it here
        result["form"].append(node)
        return result


