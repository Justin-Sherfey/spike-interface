
import json
from spikeinterface import load_extractor
from spikeinterface.sorters import run_sorter_local

if __name__ == '__main__':
    # this __name__ protection help in some case with multiprocessing (for instance HS2)
    # load recording in container
    recording = load_extractor('/Users/jsher/spike_interface/in_container_recording.json')

    # load params in container
    with open('/Users/jsher/spike_interface/in_container_params.json', encoding='utf8', mode='r') as f:
        sorter_params = json.load(f)

    # run in container
    output_folder = '/Users/jsher/spike_interface/kilosort2_output'
    sorting = run_sorter_local(
        'kilosort2', recording, output_folder=output_folder,
        remove_existing_folder=False, delete_output_folder=False,
        verbose=True, raise_error=True, with_output=True, **sorter_params
    )
    sorting.save_to_folder(folder='/Users/jsher/spike_interface/kilosort2_output/in_container_sorting')
