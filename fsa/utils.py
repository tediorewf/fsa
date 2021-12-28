
def replace_multiple(base: str,
                     replaceables: 'list[str]',
                     replacement: str) -> str:
    for replaceable in replaceables:
        base = base.replace(replaceable, replacement)
    return base
