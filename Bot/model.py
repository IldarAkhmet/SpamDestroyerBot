import torch
import torch.nn.functional as F
import torch.nn as nn


def get_model():
    model = torch.load('TextCNN/textcnn_spamdestroyer.pth')

    return model


class TextCNN(nn.Module):
    def __init__(self, vocab_size: int, embedding_dim: int, pad_idx):
        super().__init__()

        # embedding(кол-во слов в словаре+паддинг, размерность эмбеддинга, паддинг индекс)
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=pad_idx)

        # список сверток(на выходе они будут объеденены для входа в полносвязные слои)
        self.convs = nn.ModuleList(
            [
                nn.Conv2d(
                    in_channels=1,  # принимает 1 канал
                    out_channels=64,  # отдает 64 канала
                    kernel_size=(fs, embedding_dim),  # размер ядра
                    stride=2  # шаг страйда
                )
                for fs in [2, 3, 4]
            ]
        )
        # полносвязные слои
        self.fc = nn.Linear(3 * 64, 100)  # полносвязный слой из 5*64 входных нейронов и 100 выходных
        #         self.fc2 = nn.Linear(100, 10)
        self.fc3 = nn.Linear(100, 1)  # слой из 100 входных и 1 выходного

        self.batchnorm = nn.BatchNorm2d(64)  # слой нормализации

        self.dropout = nn.Dropout(
            0.5)  # 1/p * x * m 0.5 вероятность выключить нейрон(будем исключать взаимоадаптацию нейронов при обучении)

    def forward(self, x):
        x = self.embedding(x)  # переводим объект в эмбеддинг
        x = x.unsqueeze(1)  # добавим размерность(измерение канала) для свертки

        x = [F.relu(conv(x)).squeeze(3) for conv in
             self.convs]  # пропускаем через свертки через функцию активации и уберем размерность

        x = [F.max_pool1d(_, _.shape[2]).squeeze(2) for _ in x]  # делаем пулинг по длине, убираем ненужную размерность

        x = self.dropout(torch.cat(x, dim=1))  # применяем дропаут
        x = self.fc(x)
        x = self.dropout(x)
        #         x = self.fc2(x)
        #         x = self.dropout(x)

        return self.fc3(x)

