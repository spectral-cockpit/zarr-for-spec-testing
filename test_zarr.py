import os
import zarr

store = zarr.DirectoryStore('data/example.zarr')

a = zarr.create(shape=(20, 20), chunks=(10, 10), dtype='i4',
                fill_value=42, compressor=zarr.Zlib(level=1),
                store=store, overwrite=True)