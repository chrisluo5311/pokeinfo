---
name: pokeinfo
description: Query Pokémon information from PokéAPI. Use when the user wants to look up Pokémon details by name or ID, including stats, abilities, types, moves, sprites, and cries. Triggers on requests like "get info about [pokemon]", "what is [pokemon]", "pokemon stats", or any query related to Pokémon data retrieval.
---

# Pokeinfo

Query detailed Pokémon information from the PokéAPI (https://pokeapi.co).

## User Commands

- `/pokeinfo <pokemon_name_or_id>` - Query Pokémon information by name or ID
- `/pokeinfo <pokemon_name_or_id> --voice` - Get Pokémon cry as Telegram voice message

## Quick Start

Use the bundled script to fetch and format Pokémon data:

```bash
python3 scripts/pokeinfo.py <pokemon_name_or_id>
```

Examples:
```bash
python3 scripts/pokeinfo.py pikachu
python3 scripts/pokeinfo.py charizard
python3 scripts/pokeinfo.py 1          # Bulbasaur by ID
```

## What the Script Returns

- **Basic info**: ID, name, height, weight, base experience
- **Types**: Elemental type(s) (e.g., Electric, Fire/Flying)
- **Abilities**: Regular and hidden abilities
- **Stats**: HP, Attack, Defense, Special Attack, Special Defense, Speed
- **Sprites**: Official artwork URL
- **Cries**: Latest cry audio URL
- **Level-up moves**: Learnset for the most recent game version (limited to 20 moves)

## Voice Message (Pokémon Cry)

The script can convert Pokémon cries to Telegram-compatible voice messages:

```bash
python3 scripts/pokeinfo.py pikachu --voice
```

**Output:**
```json
{"voice_path": "/tmp/pokeinfo_cry_25_opus.ogg", "name": "Pikachu", "id": 25}
```

**How it works:**
- PokeAPI provides cries in **OGG Vorbis** format (~32728 Hz)
- Telegram voice messages require **OGG Opus** format (48000 Hz)
- The script automatically downloads, resamples, and converts the audio

**Voice Dependencies:**
```bash
pip install soundfile scipy
```

**AI Integration:** When `--voice` is used, parse the JSON output and send the voice file via the messaging tool.

## API Details

- **Base URL**: `https://pokeapi.co/api/v2/pokemon/{name_or_id}`
- **Method**: GET only (consumption-only API)
- **No authentication** required
- **Rate limiting**: None, but cache responses when possible

## Key Response Fields

| Field | Description |
|-------|-------------|
| `id` | National Pokédex number |
| `name` | Pokémon name (lowercase, hyphenated) |
| `height` | Decimeters (divide by 10 for meters) |
| `weight` | Hectograms (divide by 10 for kg) |
| `base_experience` | Base XP yield when defeated |
| `types` | Array of type slots with `type.name` |
| `abilities` | Array with `ability.name`, `is_hidden` flag |
| `stats` | Array of 6 stats with `stat.name` and `base_stat` |
| `sprites.other.official-artwork.front_default` | Best quality sprite |
| `cries.latest` | Cry audio file URL |
| `moves` | Learnable moves with version group details |

## Notes

- Pokémon names are case-insensitive in the API
- Use hyphenated names for forms (e.g., `mega-charizard-x`, `tapu-koko`)
- The API returns 404 if the Pokémon does not exist
- For evolution chains, species details, or other data, see the full PokéAPI docs at https://pokeapi.co/docs/v2

## Resources

### scripts/
- `pokeinfo.py` - Main script to fetch and display Pokémon information
