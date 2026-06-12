import json
from genai_craft import GenAIcraft, GeneratedAsset

def test_generate_code():
    genai_craft = GenAIcraft()
    prompt = "medieval castle with towers"
    code = genai_craft.generate_code(prompt)
    assert code.startswith("using UnityEngine;")

def test_generate_model():
    genai_craft = GenAIcraft()
    prompt = "medieval castle with towers"
    model = genai_craft.generate_model(prompt)
    assert model.endswith(".fbx")

def test_generate_asset():
    genai_craft = GenAIcraft()
    prompt = "medieval castle with towers"
    asset = genai_craft.generate_asset(prompt)
    assert isinstance(asset, GeneratedAsset)

def test_save_asset(tmp_path):
    genai_craft = GenAIcraft()
    prompt = "medieval castle with towers"
    asset = genai_craft.generate_asset(prompt)
    filename = tmp_path / "generated_asset.json"
    genai_craft.save_asset(asset, str(filename))
    with open(filename, "r") as f:
        data = json.load(f)
    assert data["code"].startswith("using UnityEngine;")
    assert data["model"].endswith(".fbx")
