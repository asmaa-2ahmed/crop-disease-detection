import os
from dotenv import load_dotenv

load_dotenv()  # Ensure this is called before accessing environment variables

APP_NAME = os.getenv("APP_NAME", default="MyApp")
APP_VERSION = os.getenv("APP_VERSION", default="1.0.0")
APP_DESCRIPTION = os.getenv("APP_DESCRIPTION", default="A sample application")

# Calculate base directory as the parent of src
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
TRAIN_DATASET_PATH = os.path.join(BASE_DIR, "src/assets/dataset/train")
MODEL_PATH = os.path.join(BASE_DIR, 'src/assets/model_weights.h5')

# Model parameters
INPUT_SHAPE = (299, 299, 3)
NUM_CLASSES = 38
BATCH_SIZE = 32
