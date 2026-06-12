import json
from dataclasses import dataclass
from typing import List

@dataclass
class GeneratedAsset:
    code: str
    model: str

class GenAIcraft:
    def __init__(self):
        self.prompts = {}

    def generate_code(self, prompt: str) -> str:
        # Simple example of generating C# code for Unity
        code = f"using UnityEngine;\npublic class {prompt.capitalize()} : MonoBehaviour {{\n}}\n"
        return code

    def generate_model(self, prompt: str) -> str:
        # Simple example of generating a 3D model (.fbx) from a text prompt
        model = f"{prompt}.fbx"
        return model

    def generate_asset(self, prompt: str) -> GeneratedAsset:
        code = self.generate_code(prompt)
        model = self.generate_model(prompt)
        return GeneratedAsset(code, model)

    def save_asset(self, asset: GeneratedAsset, filename: str):
        with open(filename, "w") as f:
            json.dump({"code": asset.code, "model": asset.model}, f)

    def main(self):
        genai_craft = GenAIcraft()
        prompt = "medieval castle with towers"
        asset = genai_craft.generate_asset(prompt)
        genai_craft.save_asset(asset, "generated_asset.json")

if __name__ == "__main__":
    GenAIcraft().main()
