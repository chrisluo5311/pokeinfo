# Pokeinfo

> 🌐 [English](#english) | [中文](#chinese)

---

<a name="english"></a>
## English

An OpenClaw skill to query Pokémon information from [PokéAPI](https://pokeapi.co).

### Features

- Query by Pokémon **name** or **ID**
- Returns: stats, abilities, types, moves, sprites, cries
- No API key required
- Lightweight Python script

### Usage

```bash
python3 scripts/pokeinfo.py <pokemon_name_or_id>
```

Examples:
```bash
python3 scripts/pokeinfo.py pikachu
python3 scripts/pokeinfo.py charizard
python3 scripts/pokeinfo.py 1          # Bulbasaur
```

### Sample Output

```
#25 Pikachu
========================================
Height: 0.4 m
Weight: 6.0 kg
Base Experience: 112

Type(s): Electric

Abilities: Static, Lightning Rod (Hidden)

Stats:
  Hp: 35
  Attack: 55
  Defense: 40
  Special Attack: 50
  Special Defense: 50
  Speed: 90

Sprite: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png
Cry: https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/25.ogg

Level-up Moves (Yellow):
  Lv.  1 Growl
  Lv.  1 Thunder Shock
  ...
```

### Installation

```bash
clawhub install pokeinfo
```

Or manually copy the `pokeinfo/` folder to your OpenClaw `skills/` directory.

---

<a name="chinese"></a>
## 中文

用於從 [PokéAPI](https://pokeapi.co) 查詢寶可夢資訊的 OpenClaw Skill。

### 功能

- 支援以**名稱**或**編號**查詢
- 回傳：數值、特性、屬性、招式、繪圖、叫聲
- 無需 API 金鑰
- 輕量 Python 腳本

### 使用方式

```bash
python3 scripts/pokeinfo.py <pokemon_name_or_id>
```

範例：
```bash
python3 scripts/pokeinfo.py pikachu
python3 scripts/pokeinfo.py charizard
python3 scripts/pokeinfo.py 1          # 妙蛙種子
```

### 輸出範例

```
#25 Pikachu
========================================
Height: 0.4 m
Weight: 6.0 kg
Base Experience: 112

Type(s): Electric

Abilities: Static, Lightning Rod (Hidden)

Stats:
  Hp: 35
  Attack: 55
  Defense: 40
  Special Attack: 50
  Special Defense: 50
  Speed: 90

Sprite: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png
Cry: https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/25.ogg

Level-up Moves (Yellow):
  Lv.  1 Growl
  Lv.  1 Thunder Shock
  ...
```

### 安裝

```bash
clawhub install pokeinfo
```

或手動將 `pokeinfo/` 資料夾複製到 OpenClaw 的 `skills/` 目錄。

---

## License

MIT
