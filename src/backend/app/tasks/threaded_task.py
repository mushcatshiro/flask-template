import os


def tasync_sample_job(target_dir: str, fname='test'):
    full_path = os.path.join(target_dir, fname)
    if os.path.isfile(full_path):
        with open(full_path, 'a') as wf:
            wf.write('new entry')
    else:
        with open(full_path, 'w') as wf:
            wf.write('new entry')
