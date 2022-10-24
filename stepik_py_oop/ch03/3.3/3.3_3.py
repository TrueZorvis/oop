class Model:
    fields = dict()

    def query(self, **kwargs):
        self.fields = kwargs

    def __str__(self):
        if self.fields:
            return "Model: " + ", ".join([f"{k} = {v}" for k, v in self.fields.items()])
        return "Model"


model = Model()
print(model)
model.query(id=1, fio='Sergey', old=33)
print(model)
