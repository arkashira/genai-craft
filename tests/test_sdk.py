import pytest
from sdk import SDK

def test_install_unity():
    sdk = SDK("GenAI-Craft", "1.0", "Unity")
    result = sdk.install()
    assert result["status"] == "success"
    assert result["message"] == "Unity package installed"

def test_install_unreal():
    sdk = SDK("GenAI-Craft", "1.0", "Unreal")
    result = sdk.install()
    assert result["status"] == "success"
    assert result["message"] == "Unreal plugin installed"

def test_install_unsupported_engine():
    sdk = SDK("GenAI-Craft", "1.0", "Unsupported")
    with pytest.raises(ValueError):
        sdk.install()

def test_integrate():
    sdk = SDK("GenAI-Craft", "1.0", "Unity")
    result = sdk.integrate()
    assert result["status"] == "success"
    assert result["message"] == "SDK integrated with asset pipeline"

def test_get_sample_project():
    sdk = SDK("GenAI-Craft", "1.0", "Unity")
    result = sdk.get_sample_project()
    assert result["status"] == "success"
    assert result["message"] == "Sample project retrieved"
