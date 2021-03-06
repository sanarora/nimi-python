#!/usr/bin/python

import argparse
import math
import nifgen

supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='PXI1Slot2', help='Resource name of a National Instruments Arbitrary Waveform Generator')
parser.add_argument('-r', '--rate', default=100e6, type=float, help='Sample Rate (Hz)')
parser.add_argument('-s', '--samples', default=100000, type=int, help='Number of Samples')
parser.add_argument('-g', '--gain', default=1.0, type=float, help='Gain')
parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC Offset')
args = parser.parse_args()


def create_waveform_data(number_of_samples):
    waveform_data = []
    angle_per_sample = (2 * math.pi) / number_of_samples
    for i in range(number_of_samples):
        waveform_data.append(math.sin(i * angle_per_sample) * math.sin(i * angle_per_sample * 20))
    return waveform_data


waveform_data = create_waveform_data(args.samples)
with nifgen.Session(args.name) as session:
    session.output_mode = nifgen.OutputMode.NIFGEN_VAL_OUTPUT_ARB  # TODO(marcoskirsch): name to change per #553
    session.configure_arb_waveform(session.create_waveform_f64(waveform_data), args.gain, args.offset)
    with session.initiate():
        try:
            input("Press Enter to abort generation...")
        except SyntaxError:
            pass

