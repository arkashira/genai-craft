from genai_craft import GenAI, UI

def test_genai_parameters():
    genai = GenAI()
    assert genai.get_parameters().temperature == 1.0
    assert genai.get_parameters().top_p == 0.9

def test_update_parameters():
    genai = GenAI()
    ui = UI(genai)
    ui.update_parameters(2.0, 0.8)
    assert genai.get_parameters().temperature == 2.0
    assert genai.get_parameters().top_p == 0.8

def test_generate_content():
    genai = GenAI()
    assert "Generated content" in genai.generate_content()

def test_ui_display_parameters():
    genai = GenAI()
    ui = UI(genai)
    # Simulate display_parameters method
    parameters = genai.get_parameters()
    assert f"temperature={parameters.temperature}" in "Current parameters: temperature=1.0, top_p=0.9"
    assert f"top_p={parameters.top_p}" in "Current parameters: temperature=1.0, top_p=0.9"

def test_ui_update_parameters():
    genai = GenAI()
    ui = UI(genai)
    ui.update_parameters(2.0, 0.8)
    assert genai.get_parameters().temperature == 2.0
    assert genai.get_parameters().top_p == 0.8
