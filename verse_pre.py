import os
import shutil
import argparse

def extract_and_rename_ct_files(source_dir, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for case_folder in os.listdir(source_dir):
        case_path = os.path.join(source_dir, case_folder)
        if os.path.isdir(case_path):
            ct_file_path = os.path.join(case_path, 'ct.nii.gz')
            if os.path.exists(ct_file_path):
                new_ct_filename = f"{case_folder}_ct.nii.gz"
                new_ct_file_path = os.path.join(save_dir, new_ct_filename)
                
                # Copy and rename the ct.nii.gz file to the destination directory
                shutil.copy(ct_file_path, new_ct_file_path)
            

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', default='', help='The path of totalsegmentator data')
    parser.add_argument('--save_dir', default='', help='The saving path after reorganizing')
    args = parser.parse_args()
    
    extract_and_rename_ct_files(args.data_path, args.save_dir)

if __name__ == '__main__':
    main()

