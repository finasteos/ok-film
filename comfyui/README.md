# ComfyUI Local Video Generation Setup

This directory is for setting up a local video generation pipeline using ComfyUI.

## 1. Recommended Model: AnimateDiff-Lightning

For the fast, high-quality anime style we are targeting, the **AnimateDiff-Lightning** models are the current state-of-the-art. They are designed for speed and can generate short clips in seconds.

**Download the following model:**
- **Model:** `ByteDance/AnimateDiff-Lightning`
- **File:** `animatediff_lightning_4step_t2v.safetensors`
- **Hugging Face Link:** [https://huggingface.co/ByteDance/AnimateDiff-Lightning/blob/main/animatediff_lightning_4step_t2v.safetensors](https://huggingface.co/ByteDance/AnimateDiff-Lightning/blob/main/animatediff_lightning_4step_t2v.safetensors)

## 2. Installation

1.  Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
2.  Place the downloaded `animatediff_lightning_4step_t2v.safetensors` file into the `ComfyUI/models/animatediff_models/` directory.
3.  Load the `workflow.json` from this directory into the ComfyUI interface.

This setup will give you a powerful, local, and fast video generation pipeline, perfect for bringing the OK Film manuscript to life.