def build_model(input_shape, num_classes):
    """
    Builds a neural network model for image classification.
    
    Args:
        input_shape (tuple): Shape of input images as (width, height, channels).
        num_classes (int): Number of output classes for classification.

    Returns:
        keras.Model: Compiled model ready for training.
    """
    pass

def train_model(data_dir, img_size=(224, 224), batch_size=32, epochs=10):
    """
    Trains the classification model.
    
    Args:
        data_dir (str): Path to the directory containing image data.
        img_size (tuple): Target image size as (width, height).
        batch_size (int): Number of images per batch.
        epochs (int): Number of epochs to train the model.

    Returns:
        None
    """
    pass

if __name__ == "__main__":
    train_model('data/plants', epochs=15)
