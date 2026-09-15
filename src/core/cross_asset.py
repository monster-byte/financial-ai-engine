from typing import Dict


class CrossAssetRelationships:

    def __init__(self):
        self.relationships: Dict[str, float] = {}

    def set_relationship(
        self,
        asset_a: str,
        asset_b: str,
        strength: float,
    ) -> None:

        key = self._make_key(asset_a, asset_b)

        self.relationships[key] = strength

    def get_relationship(
        self,
        asset_a: str,
        asset_b: str,
    ) -> float:

        key = self._make_key(asset_a, asset_b)

        return self.relationships.get(key, 0.0)

    def all_relationships(self) -> Dict[str, float]:
        return self.relationships.copy()

    @staticmethod
    def _make_key(
        asset_a: str,
        asset_b: str,
    ) -> str:

        return f"{asset_a}:{asset_b}"
