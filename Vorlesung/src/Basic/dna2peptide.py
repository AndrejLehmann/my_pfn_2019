#!/usr/bin/env python3
import argparse
import transcription_table

### This class is used for translating dna strings to amino acid strings
class DnaTranslator:

  import transcription_table  # for @@transcription_table
  #include TranscriptionTable

  ### Translate a dna string to an amino acid string
  def translatedna():
    if not callable(dna.to_string()):
      raise argparse.ArgumentTypeError('Class need be convertable to String.')
    mydna = dna.to_string()

    aa_sequence = String.__new__(String)
    # Translate each three-base codon into an amino acid, and append to protein
    n = 3
    for codon in [dna[i:i+n] for i in range(0, len(dna) - 2, n)]:
      aa_sequence += transcription_table[codon.upper()]
    return aa_sequence
