from genai_craft import GenAIcraft, GeneratedAsset
import json
import os

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

def test_save_asset():
    genai_craft = GenAIcraft()
    prompt = "medieval castle with towers"
    asset = genai_craft.generate_asset(prompt)
    filename = "generated_asset.json"
    genai_craft.save_asset(asset, filename)
    assert os.path.exists(filename)
    with open(filename, "r") as f:
        data = json.load(f)
        assert "code" in data and "model" in data
    os.remove(filename)
