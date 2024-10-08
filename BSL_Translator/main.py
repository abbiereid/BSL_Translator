import train_classifier
import test_classifier
import expression_capture
import dataset_creator

def build():
    expression_capture.expression_capture()
    dataset_creator.create_dataset()
    train_classifier.train_and_save_model()
    test_classifier.test_model()