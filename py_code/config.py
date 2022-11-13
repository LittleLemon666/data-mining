IMAGE_PATH = './output_image/'
MODEL_PATH = 'encoder_model'
# init loop
INIT_EPOCH = 30

INIT_EBCODER_LR = 0.01
INIT_DECODER_LR = 0.005

# train loop
EPOCH = 20
ITER = 5

ENCODER_LR = 0.01
DECODER_LR = 0.005

SCHEDULER_STEP = 10
SCHEDULER_GAMMA = 0.9

# epoch every LAMBDA_STEP, lambda *= LAMBDA_GAMMA
LAMBDA = 0.005
LAMBDA_STEP = 10
LAMBDA_MAX = 1
LAMBDA_GAMMA = 1.2


# number of sample
N = 1000
BATCH_SIZE = 64
x_dim = 2 # X
y_dim = 2 # U
embedding_dim = x_dim

DEBUG = False

# gif
SAVE_GIF = True
SAVE_STEP = 5

# check_U mode, input dimension(1d, 2d, 3d)(split by space) show U graph
CHECK_U = False