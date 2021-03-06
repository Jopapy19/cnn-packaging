import os

DATA_DIR = os.path.join("data", "GenderImages") # Searching dataset
IMAGE_SIZE = (224, 224, 3)
BATCH_SIZE = 32
EPOCHS = 10
CLASSES = 2
TRAINED_MODEL_DIR = os.path.join("VGGmodel", "models")
CHECKPOINT_DIR = os.path.join("VGGmodel", "checkpoints")
AUGMENTATION = True
BASE_LOG_DIR = "base_log_dir"
TENSORBOARD_ROOT_LOG_DIR = os.path.join(BASE_LOG_DIR, "tensorboard_log_dir")
