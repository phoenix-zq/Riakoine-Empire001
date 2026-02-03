def find_kill_zones(gaps, fvgs):
    kill_zones = []
    for gap in gaps:
        for fvg in fvgs:
            if min(gap.top, fvg.top) > max(gap.bottom, fvg.bottom):
                kill_zones.append(f"Confluence: {gap.name} + {fvg.name}")
    return kill_zones
