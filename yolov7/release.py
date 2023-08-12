import torch

# Some computations...

# Clear the GPU cache to release memory
gc.collect()
torch.cuda.empty_cache()
