import shutil
from os import makedirs
from urllib import request
from session2.classes.compressors.gzip_compressor import GzipCompressor
from session2.classes.compressors.rar_compressor import RarCompressor
from session2.classes.compressors.zip_compressor import ZipCompressor
from session2.classes.compressors.base import CompressorBase
from session2.classes.enums import CompressionType, TransferType
from session2.classes.instance_creator import create_instance
from session2.classes.transfer_adapters.ftp_adapter import FTPAdapter
from session2.classes.transfer_adapters.s3_adapter import S3Adapter

# x = ZipCompressor()

assert hasattr(CompressorBase, 'compress')


class Supplier:
    def __init__(self, addresses, compression_type, transfer_type, transfer_params):
        self.addresses = addresses
        self.compression_type = compression_type
        self.transfer_type = transfer_type
        self.transfer_params = transfer_params

    def supply(self):
        local_files = self.__download_files()
        compressed_local_path = self.__compress_files(local_files)
        self.__transfer_file(compressed_local_path)

    def __download_files(self):
        local_files = []

        for address in self.addresses:
            print(f"Downloading from {address}")
            local_path = f"tmp/{address.split('/')[-1]}"

            with request.urlopen(address) as response, open(local_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                local_files.append(local_path)



        return local_files

    def __compress_files(self, files_paths):
        output_file_path = "tmp/output.zip"
        compressor = create_instance(self.compression_type.value, output_file_path)

        with compressor:
            for file in files_paths:
                compressor.compress(file)

    def __transfer_file(self, path):
        if self.transfer_type == TransferType.FTP:
            FTPAdapter(path, **self.transfer_params).transfer()
        if self.transfer_type == TransferType.S3:
            S3Adapter(path, **self.transfer_params).transfer()


if __name__ == '__main__':
    try:
        makedirs("tmp")
    except:
        pass

    supplier = Supplier(
        addresses=["https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv",
                   "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"],
        compression_type=CompressionType.ZIP,
        transfer_type=TransferType.FTP,
        transfer_params=dict(
            server="ftp://something",
            port=20
        )
    )

    supplier.supply()

import compressors.zip