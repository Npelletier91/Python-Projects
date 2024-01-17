import torch
print(torch.__version__)

print(torch.get_default_dtype())

new_tensor = torch.Tensor([[1,2,3,], [4,5,6]])
print(new_tensor)

random_tensor_values = torch.rand(2,2)
print(random_tensor_values)

print(torch.cuda.is_available())
