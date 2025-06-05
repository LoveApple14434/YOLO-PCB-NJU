import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO

model = YOLO(f".\\runs\\detect\\train57\\weights\\best.pt")
results = model.train(data=".\\data.yaml",
                      pretrained=True,
                      epochs=100,
                      workers=0,
                      device='cuda',
                      imgsz=2160,
                      batch=-1,
                      cls=1.0,
                      cache='disk',
                      save=True,
                      lr0=0.0001,
                      scale=0.8,
                      degrees=180,
                      fliplr=0,
                      )


# train30-34: different cls weight
# train35: added epoch to 150, imgsz to 1280, copy_paste to 50%, scale to 0.8, degrees to 180
# train 26: imgsz to 2560, failed by memory
# train 37: imgsz to 1920
# train 38: imgsz 1280, copy_paste 80%
# train 39: epoch 200
# train 40: imgsz 2560 epoch 100, failed
# train 41: imgsz 2160, epoch 150, using train 37 last.pt.   too slow
# train 42: imgsz 2160, epoch 30, using train 37 last.pt
# train 43: regenerate dataset where num of types down to 5, added a test set, imgsz 1280, epoch 100, patience 15, using train 42 best.pt
# train 45: imgsz 1920, epoch 50, copy_paste 0.6, batch auto(-1), using training 43 last.pt
# train 46: delete copy_paste arg, using training 45 last.pt
# train 47: using train 45 last.pt, cls down to 0.5, cache='disk'.      early stop by patience
# train 48: using train 47 last.pt, default patience
# train 49: using train 48 last.pt, imgsz 1920, 30 epochs, cls=0.2
# train 50: from train 49 last.pt, another 50 epochs
# train 51: from train 49 last.pt, imgsz 2176, another 30 epochs
# train 52: continue train 51, another 100 epoch
# train 54: continue train 52, another 200 epoch.             eraly stop by patience 100
# train 55: imgsz 2560, using train 54 best.pt          failed by memory
# train 57: continue 54, imgsz 2160, 150 epoch          no improve1
# train 64: try small object detection head at 1920 imgsz, 20 epoch, using train 54 best.ptr         failed.
# train 67: continue 57 best, 100 epoch @ 1280 imgsz, lr0 0.001->0.0001
# train 68: continue 57 best, 100 epoch @ 1280 imgsz, lr0 0.01
# train 69: continue 57 best, 100 epoch @ 2160 imgsz, lr0 0.0001, cls 1.0