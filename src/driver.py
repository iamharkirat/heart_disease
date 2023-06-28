import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
import logging
import sys
import os
import os.path as path

# check for windows or linux os
if os.name == 'nt':
    sys.path.insert(0, path.abspath(path.join(__file__, "../../..")))
else:
    sys.path.append(path.abspath(path.join(__file__, "../../..")))

from heart_disease.src.data import DataExtractor as de
from heart_disease.src.models import LogisticRegression as lr
from heart_disease.src.processing import PreProcessor as pre
import heart_disease.src.processing.read_yaml as yml

warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.info('--' * 5 + 'Loading config file' + '--' * 5)
    config = yml.yaml_loader()
    logger.info('--' * 5 + 'Completed loading config file!' + '--' * 5)
    
    input_path = '.'
    logger.info('--' * 5 + 'Input path' + '--' * 5 + input_path)
    
    logger.info('--' * 5 + 'Loading paths dictionary' + '--' * 5)
    paths_dict = pd.read_csv(input_path + config['file_paths']['path_params'])
    paths_dict['path'] = input_path + paths_dict.iloc[:, [1]]
    logger.info('--' * 5 + "Printing paths_dict" + '--' * 5)
    logger.info(paths_dict)
    paths_dict = dict(paths_dict.values.tolist())
    
if __name__ == '__main__':
    main()