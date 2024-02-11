import torch


def get_model():
    model = torch.load('TextCNN/textcnn_spamdestroyer.pth')

    return model
