import os
import tensorflow as tf
import numpy as np
import utils.config as config


def save_vgg_16_model(input_shape=config.IMAGE_SIZE):
    model = tf.keras.applications.vgg16.VGG16(
        input_shape=input_shape,
        weights="imagenet",
        include_top=False

    )
    model.save("original_vgg_base.h5")
    print("Base model is saved")

def load_base_model():
    model = tf.keras.models.load_model("original_vgg_base.h5")
    print("loading original base model ")
    model.summary()
    return model

def custom_model(CLASSES=config.CLASSES, freeze_all=True, freeze_till=None):
    model = load_base_model() #loaded base model
    
    # Freeze weights...
    if freeze_all:
        for layer in model.layers:
            layer.trainable=False
    elif (freeze_till is not None) and (freeze_till > 0):
        for layer in model.layers[:freeze_till]:
            layer.trainable = False
    
    # Add custom Layers...
    flatten_in = tf.keras.layers.Flatten()(model.output)
    prediction = tf.keras.layers.Dense(
        units=CLASSES,
        activation="softmax"
    )(flatten_in)

    full_model = tf.keras.models.Model(
        inputs=model.input,
        outputs=prediction
    )
    print("Custom model summary")
    full_model.summary()

    full_model.compile(
        optimizer = tf.keras.optimizers.SGD(lr=0.005, momentum=0.9),
        loss = tf.keras.losses.CategoricalCrossentropy(),
        metrics = ["accuracy"]

    )
    return full_model

def callbacks(base_dir="."):

    # Tensorboard callbacks
    base_log_dir = config.BASE_LOG_DIR
    tensorboard_log_dir = os.path.join(base_log_dir, "tensorboard_log_dir")
    os.makedirs(tensorboard_log_dir, exist_ok=True) #Ignore if already exits


    tensorboard_cb = tf.keras.callbacks.TensorBoard(log_dir=tensorboard_log_dir)

    # Checkpoint callbacks
    checkpoint_file = os.path.join(config.CHECKPOINT_DIR, "vgg16_model_checkpoint.h5")
    os.makedirs(config.CHECKPOINT_DIR, exist_ok=True) # Create checkpoint directory if not exists

    checkpoint_cb = tf.keras.callbacks.ModelCheckpoint(
        filepath = checkpoint_file,
        save_best_only=True
    )
    callback_list = [tensorboard_cb, checkpoint_cb]
    
    return callback_list

if __name__ == '__main__':
    custom_model()
