from dna2aa import dna2peptide  # from section 13
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['get'])
def translate_form():
  seq = request.args.get('seq')
  if seq is None:
    return render_template('translate.html',
                           input_sequence='')
  peptide = dna2peptide(seq)
  return render_template('translate.html',
                         input_sequence=seq,
                         output=peptide)
