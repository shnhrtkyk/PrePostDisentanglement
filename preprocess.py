import os
import argparse


def preprocess_folders(args):
    if not os.path.exists(args.dest):
        os.mkdir(args.dest)

    trainA_path = os.path.join(args.root, 'trainA')
    trainB_path = os.path.join(args.root, 'trainB')
    testA_path = os.path.join(args.root, 'testA')
    testB_path = os.path.join(args.root, 'testB')
    
    trainA = os.listdir(os.path.join(args.root, 'trainA'))
    trainB = os.listdir(os.path.join(args.root, 'trainB'))
    testA = os.listdir(os.path.join(args.root, 'testA'))
    testB = os.listdir(os.path.join(args.root, 'testB'))

    with open(os.path.join(args.dest, 'testA.txt'), 'w') as f:
        for i, _img in enumerate(testA):
            if i == len(testA) - 1:
                f.write("%s" % os.path.join(testA_path, _img))
            else:
                f.write("%s\n" % os.path.join(testA_path, _img))

    with open(os.path.join(args.dest, 'testB.txt'), 'w') as f:
        for i, _img in enumerate(testB):
            if i == len(testB) - 1:
                f.write("%s" % os.path.join(testB_path, _img))
            else:
                f.write("%s\n" % os.path.join(testB_path, _img))

    with open(os.path.join(args.dest, 'trainA.txt'), 'w') as f:
        for i, _img in enumerate(trainA):
            if i == len(trainA) - 1:
                f.write("%s" % os.path.join(trainA_path, _img))
            else:
                f.write("%s\n" % os.path.join(trainA_path, _img))

    with open(os.path.join(args.dest, 'trainB.txt'), 'w') as f:
        for i, _img in enumerate(trainB):
            if i == len(trainB) - 1:
                f.write("%s" % os.path.join(trainB_path, _img))
            else:
                f.write("%s\n" % os.path.join(trainB_path, _img))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="",
                        help="path to the celeba folder, or if you\'re using another dataset this should be the path to the root")
    parser.add_argument("--dest", default="", help="path to the destination folder")
    parser.add_argument("--attributes", default="", help="path to the attributes file")
    parser.add_argument("--num_test_imgs", default=64, help="number of images in the test set")
    parser.add_argument("--config", default="glasses", help="configs available: glasses, mouth, beard")
    parser.add_argument("--custom", default=32, help="use a custom celeba attribute")


    args = parser.parse_args()
    
    preprocess_folders(args)
