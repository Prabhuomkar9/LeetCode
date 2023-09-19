class Solution:
    def encode(self, decoded: List[str]) -> str:
        encoded = ""

        for st in decoded:
            encoded += f"{len(st)}.{st}"

        return encoded

    def decode(self, encoded: str) -> list[str]:
        decoded = []

        while encoded != "":
            start = encoded.find(".")
            length = int(encoded[:start])
            encoded = encoded[start + 1 :]

            decoded.append(encoded[:length])
            encoded = encoded[length:]

        return decoded
