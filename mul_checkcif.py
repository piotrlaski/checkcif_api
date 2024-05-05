from checkcif_api import *

def dir_checkcif(cif_directory:os.PathLike) -> None:
    cif_files = []
    out_pdf_files = []
    for filename in os.listdir(cif_directory):
        if filename[-4:] == '.cif':
            cif_path = os.path.join(cif_directory, filename)
            cif_files.append(cif_path)
            out_pdf_path = os.path.join(cif_directory, filename[:-4] + '.pdf')
            out_pdf_files.append(out_pdf_path)

    for cif_file, out_pdf_path in zip(cif_files, out_pdf_files):
        get_pdf(in_cif_file=cif_file, out_pdf_file=out_pdf_path)


if __name__ == '__main__':
    cif_directory = r'C:\Users\piotr\Documents\working_dirs_lapek\checkcif_api\example_files'
    dir_checkcif(cif_directory=cif_directory)