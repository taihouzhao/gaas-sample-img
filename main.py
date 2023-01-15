from diffusers import StableDiffusionPipeline, DDIMScheduler
import torch
from tqdm.auto import tqdm
import hashlib

def promptMagic(category):
    return {
        "prompt": f"a portrait photo of asian {category}, looking at camera, extra details, 4k, realistic photo",
        "negative_prompt": "ugly face, blurry, bad teeth, big teeth, dark skin, overweight, strong beard, old, fat, closed eye, missing, Poorly drawn face, Morbid, half face",
        "num_inference_steps": 75,
        "guidance_scale": 8,
        "height": 512,
        "width": 512,
        "num_images_per_prompt": 1,
    }

def _dummy(images, **kwargs):
    return images, False

def inference(model_name, category):
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16).to("cuda")
    pipe.safety_checker = _dummy  # disable NSFW
    pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
    pipe.set_progress_bar_config(disable=True)
    prompt = promptMagic(category)
    num = 256
    for idx in tqdm(range(num), desc="Generate images", total=num):
        img = pipe(**prompt).images[0]
        hash_image = hashlib.sha1(img.tobytes()).hexdigest()
        temp_name = f"/img/{category}/{idx}-{hash_image}.png"
        img.save(temp_name)

if __name__ == "__main__":
    inference("runwayml/stable-diffusion-v1-5", "woman")
    inference("runwayml/stable-diffusion-v1-5", "man")
