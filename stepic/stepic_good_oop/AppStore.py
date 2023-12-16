class AppStore:
    def __init__(self):
        self.apps = {}

    def add_application(self, app):
        self.apps[id(app)] = app

    def remove_application(self, app):
        self.apps.pop(id(app))

    def block_application(self, app):
        obj = self.apps.get(id(app),False)
        if not obj:
            return False
        obj.blocked = True
        return True

    def total_apps(self):
        return len(self.apps)

class Application:
    def __init__(self, name, blocked=False) -> None:
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
print(store.total_apps())