from datasets import load_dataset
from diarizers.data.synthetic import SyntheticDataset

if __name__ == '__main__':

    config = {
        "num_samples": 500,
        "audio_file_length": 1.0,
        "batch_size": 8, 
        "std_concatenate": 0.5,
        "sample_rate": 16000,
        "denoise": False,
        "normalize": False,
        "augment": True,
        "silent_regions": {
            "silent_regions": True,
            "silence_duration": 5,
            "silence_proba": 0.1,
        },
        "bn_path": "/home/kamil/datasets/wham_noise/wham_noise/tr",
        "ir_path": "/home/kamil/datasets/MIT-ir-survey",
        "short_audio_threshold":2.5, 
    }

    common_voice = load_dataset(
        "mozilla-foundation/common_voice_16_1", "ja", num_proc=24
    )
    speaker_column_name = "client_id"
    audio_column_name = "audio"

    spd_dataset = SyntheticDataset(
        common_voice,
        speaker_column_name,
        audio_column_name,
        config,
    ).create_spd_dataset(num_proc=24)

    # spd_dataset.push_to_hub("kamilakesbi/cv_for_spd_ja_2k_rayleigh")