"""
    AUTHOR: Jopapy19
    Date: 2021/03-13 UM907 32
"""

import os
import utils.config as config
import tensorflow as tf
import utils.data_management as dm
import time
from utils import model
from PIL import Image


def get_unique_model_name(specific_name="VGG16_model"):
    model_fileName = time.strftime(f"{specific_name}_at_%Y%m%d_%H%M%S.h5")
    os.makedirs(config.TRAINED_MODEL_DIR, exist_ok=True)
    model_file_path = os.path.join(config.TRAINED_MODEL_DIR, model_fileName)
    return model_file_path

def train():
    my_model = model.custom_model()
    callbacks = model.callbacks()
    train_generator, valid_generator = dm.train_valid_generator()

    """
    STEPS FOR EPOCHS 
    train_generator.samples = 256
    batch_size = 16

    Fit and save the model
    """
    steps_per_epoch = train_generator.samples // train_generator.batch_size   
    validation_steps =  valid_generator.samples // valid_generator.batch_size

    my_model.fit(
        train_generator, 
        validation_data=valid_generator,
        epochs=config.EPOCHS, 
        steps_per_epoch=steps_per_epoch, 
        validation_steps=validation_steps, 
        callbacks=callbacks
        )

    
    #Saving our model
    model_file_path = get_unique_model_name()
    my_model.save(model_file_path)
    print(f"Saving model at\n ==>{model_file_path}")



if __name__ == "__main__":    
    train()