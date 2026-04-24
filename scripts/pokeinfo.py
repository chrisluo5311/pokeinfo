#!/usr/bin/env python3
"""
Pokeinfo - Fetch and format Pokémon information from PokéAPI.
Usage: python3 pokeinfo.py <pokemon_name_or_id>
"""

import sys
import json
import urllib.request
import urllib.error

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon(name_or_id):
    """Fetch Pokémon data from PokéAPI."""
    url = f"{BASE_URL}/{name_or_id.lower().strip()}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; Pokeinfo/1.0)'
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Pokémon '{name_or_id}' not found.")
        else:
            print(f"Error: HTTP {e.code} - {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def format_pokemon(data):
    """Format Pokémon data into readable output."""
    lines = []
    
    # Header
    lines.append(f"#{data['id']} {data['name'].title()}")
    lines.append("=" * 40)
    
    # Basic Info
    lines.append(f"Height: {data['height'] / 10:.1f} m")
    lines.append(f"Weight: {data['weight'] / 10:.1f} kg")
    lines.append(f"Base Experience: {data['base_experience']}")
    lines.append("")
    
    # Types
    types = [t['type']['name'].title() for t in data['types']]
    lines.append(f"Type(s): {', '.join(types)}")
    lines.append("")
    
    # Abilities
    abilities = []
    for a in data['abilities']:
        name = a['ability']['name'].replace('-', ' ').title()
        if a['is_hidden']:
            name += " (Hidden)"
        abilities.append(name)
    lines.append(f"Abilities: {', '.join(abilities)}")
    lines.append("")
    
    # Stats
    lines.append("Stats:")
    for stat in data['stats']:
        stat_name = stat['stat']['name'].replace('-', ' ').title()
        lines.append(f"  {stat_name}: {stat['base_stat']}")
    lines.append("")
    
    # Sprites
    sprite_url = data['sprites']['other']['official-artwork']['front_default']
    if not sprite_url:
        sprite_url = data['sprites']['front_default']
    if sprite_url:
        lines.append(f"Sprite: {sprite_url}")
    
    # Cries
    cry_url = data['cries'].get('latest')
    if cry_url:
        lines.append(f"Cry: {cry_url}")
    
    lines.append("")
    
    # Moves (level-up moves only, grouped by version)
    level_up_moves = {}
    for move_entry in data['moves']:
        move_name = move_entry['move']['name'].replace('-', ' ').title()
        for detail in move_entry['version_group_details']:
            if detail['move_learn_method']['name'] == 'level-up':
                version = detail['version_group']['name'].replace('-', ' ').title()
                level = detail['level_learned_at']
                if version not in level_up_moves:
                    level_up_moves[version] = []
                level_up_moves[version].append((level, move_name))
    
    if level_up_moves:
        # Pick the most recent version with moves
        recent_version = sorted(level_up_moves.keys())[-1]
        moves = sorted(level_up_moves[recent_version], key=lambda x: x[0])
        lines.append(f"Level-up Moves ({recent_version}):")
        for level, move_name in moves[:20]:  # Limit to 20 moves
            lines.append(f"  Lv.{level:>3} {move_name}")
        if len(moves) > 20:
            lines.append(f"  ... and {len(moves) - 20} more")
        lines.append("")
    
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pokeinfo.py <pokemon_name_or_id>")
        sys.exit(1)
    
    name_or_id = sys.argv[1]
    data = fetch_pokemon(name_or_id)
    print(format_pokemon(data))

if __name__ == "__main__":
    main()
