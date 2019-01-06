import os

root = 'data'
train_dir='train'
test_dir='test'
image_dir = os.path.join(root, train_dir)

annotation_file=os.path.join(root,'annotations.json')

train_imageset_fn=os.listdir(image_dir)
test_imageset_fn=os.listdir(os.path.join(root,test_dir))

train_imageset_fn=list(map(lambda x:os.path.join(train_dir,x),train_imageset_fn))

val_image_dir=os.path.join(root, test_dir)
val_imageset_fn = list(map(lambda x:os.path.join(test_dir,x),test_imageset_fn))
image_ext = '.jpg'

backbone = 'resnet101'
classes = ['s', 'z', 'j', 'l', 'd']

# TODO change with dataset
# mean, std = (0.499, 0.523, 0.532), (0.200, 0.202, 0.224)
mean, std = (0.485, 0.456, 0.406), (0.229, 0.224, 0.225)

scale =None

batch_size = 8
lr = 1e-4
momentum = 0.9
weight_decay =0.0002
num_epochs = 70
lr_decay_epochs = [10]
num_workers = 8
width,height=512,512
eval_while_training = True
eval_every = 2
