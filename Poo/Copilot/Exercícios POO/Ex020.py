class PLaylist:
    def __init__(self, musicas):
        self.musicas = musicas

    def __len__(self):
        return len(self.musicas)

p1 = PLaylist(['Rock', 'Pop', 'Jazz'])
print(len(p1))