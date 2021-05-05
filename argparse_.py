import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Experiment')
    parser.add_argument('--multi_thread', default=True, type=bool)
    parser.add_argument('--exp_id', default=0, type=int)
    for i in range(10):
        args = parser.parse_args()
        args.exp_id = i
        print("args.exp_id is", args.exp_id)
