from my_darknet import *


class darknet:
    def __init__(self, cfg, weights, meta):
        self.net = load_net(cfg.encode('utf-8'), weights.encode('utf-8'), 0)
        self.meta = load_meta(meta.encode('utf-8'))

    def predict(self, imagePath):
        image = load_image(imagePath.encode('utf-8'), 0, 0)
        return classify(self.net, self.meta, image)


if __name__ == '__main__':
    path_Cfg = "/home/can/Proje22temmuz/Zebramo.cfg"
    path_Weights = "/home/can/Proje22temmuz/backup/Zebramo_4.weights"
    path_Meta = "/home/can/Proje22temmuz/Zebramo.data"
