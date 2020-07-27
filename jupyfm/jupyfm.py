from notebook.services.contents.largefilemanager import LargeFileManager
import os
from tornado import web
import shutil

class Jupyfm(LargeFileManager):
    def rename_file(self, old_path, new_path):
        try:
            with self.perm_to_403():
                if os.path.isdir(old_path):
                    for i in os.scandir(path=old_path):
                        if i.is_dir():
                            raise web.HTTPError(500, u'Renaming a folder with subfolders is not allowed: %s' % (old_path))
        except web.HTTPError:
            raise
        except Exception as e:
            raise web.HTTPError(500, u'Unknown error renaming file %s %s' % (old_path, e))

        return super().rename_file(old_path, new_path)

