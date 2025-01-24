# Run-Length-Changed-Encoding-RLCE-
Run Length Encoding (RLE), but reduces item size by only including the RL when it changes (or, in order to support any input data, when a item has similar formatting).

Overall, list size will always be equivalent to RLE, but item length will be either equivalent, or take up less space when it can. So far after using this with custom image data, i've seen a ~30% reduction in item length using this compared to traditional RLE :3
