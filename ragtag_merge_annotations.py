"""

GOAL: Merge AGP file annotations to give clear description of 
entire scaffolding process in BED file format

"""
import sys
import argparse

import pysam

from ragtag_utilities.utilities import reverse_complement
from ragtag_utilities.AGPFile import AGPFile



def main():
  parser = argparse.ArgumentParser(description="Build BED assembly annotations from a set of AGP v2.1 file.", usage="ragtag.py agp2fa <scaffolds.agp> <components.fasta>")
  parser.add_argument("sample", metavar="<sample_name>", nargs='?', default="sample", type=str, help="Assembled Sample Name")
  parser.add_argument("longstitch_dir", metavar="</path/to/longstitch_dir>", nargs='?', default="./", type=str, help="Longstitch gap-filling directory")
  parser.add_argument("rt_scaffold_dir", metavar="</path/to/ragtag_scaffold_dir>", nargs='?', default="", type=str, help="RagTag Scaffold output directory")
  parser.add_argument("rt_patch_dir", metavar="</path/to/ragtag_patch_dir>", nargs='?', default="", type=str, help="RagTag Patch output directory")
  parser.add_argument("components", metavar="<components.fasta>", nargs='?', default="", type=str, help="component FASTA file (can be uncompressed or bgzipped)")
  
  args = parser.parse_args()
  if not args.longstitch_dir or not args.components:
    parser.print_help()
    sys.exit()
  """
  This is built out for the file storage system I have to make the defaults easy for me. If you don't use the 
  same system, specify the input directories manually. If you want to make it easy: 
  /path/to/longstitch_dir/
    | - ragtag_scaffold/
    | - ragtag_output/
    |    | - ragtag.patch.ctg.agp
    |    | - ragtag.patch.rename.agp
    |    \ - ragtag.patch.agp
    | - {args.sample}.*.ntLink.scaffolds.gap_fill.fa.agp
    \ - {args.sample}.*.trimmed_scafs.agp
    
    
  """
  
  ls_dir = args.longstitch_dir
  components_file = args.components

  if not args.rt_scaffold_dir:
    rt_scaffold_dir = "/".join((ls_dir, "ragtag_scaffold"))
  if not args.rt_patch_dir:
    rt_scaffold_dir = "/".join((ls_dir, "ragtag_output"))
  


if __name__ == "__main__":
  main()

