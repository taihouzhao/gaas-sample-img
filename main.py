from diffusers import StableDiffusionPipeline, DDIMScheduler
import torch
from tqdm.auto import tqdm


def promptMagic(category):
    return {
        "prompt": f"a photo of {category}, looking at camera, extra details, 4k, realistic photo",
        "negative_prompt": "ugly face, blurry, bad teeth, big teeth, dark skin, overweight, strong beard, old, fat, closed eye, missing, Poorly drawn face, Morbid, half face",
        "num_inference_steps": 100,
        "guidance_scale": 7.5,
        "height": 512,
        "width": 512,
        "num_images_per_prompt": 1,
    }


def inference(model_name, category):
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16).to("cuda")
    pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
    pipe.set_progress_bar_config(disable=True)
    prompt = promptMagic(category)
    num = 4
    for idx in tqdm(range(num), desc="Generate images", total=num):
        img = pipe(**prompt).images[0]
        temp_name = f"/img/{category}/{idx}.png"
        img.save(temp_name)

if __name__ == "__main__":
    inference("runwayml/stable-diffusion-v1-5", "woman")
    inference("runwayml/stable-diffusion-v1-5", "man")