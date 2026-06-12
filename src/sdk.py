import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class SDK:
    name: str
    version: str
    engine: str

    def install(self) -> Dict[str, str]:
        if self.engine == "Unity":
            return self._install_unity()
        elif self.engine == "Unreal":
            return self._install_unreal()
        else:
            raise ValueError("Unsupported engine")

    def _install_unity(self) -> Dict[str, str]:
        # Simulate Unity package installation
        return {"status": "success", "message": "Unity package installed"}

    def _install_unreal(self) -> Dict[str, str]:
        # Simulate Unreal plugin installation
        return {"status": "success", "message": "Unreal plugin installed"}

    def integrate(self) -> Dict[str, str]:
        # Simulate integration with engine's asset pipeline
        return {"status": "success", "message": "SDK integrated with asset pipeline"}

    def get_sample_project(self) -> Dict[str, str]:
        # Simulate retrieval of sample project
        return {"status": "success", "message": "Sample project retrieved"}
