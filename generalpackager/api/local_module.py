
from generallibrary import ObjInfo


class LocalModule:
    def __init__(self, module):
        self.module = module
        self.objInfo = ObjInfo(self.module)
        assert self.objInfo.is_module()

    def get_attributes(self, parent_objInfo=None):
        if parent_objInfo is None:
            parent_objInfo = self.objInfo

        for objInfo in parent_objInfo:
            if objInfo.name.startswith("_") or (not objInfo.from_class() and not objInfo.from_module()):  # 3 HERE ** Finish origins in ObjInfo
                objInfo.remove()
            else:
                print(objInfo)
                self.get_attributes(parent_objInfo=objInfo)

        print(self.objInfo.get_all())

