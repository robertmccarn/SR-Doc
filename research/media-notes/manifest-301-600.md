# Media audit — manifest entries 301–600
## Completed 2026-11-20

### Scope and method
- Reviewed manifest records 301–600 in original order.
- Matched every record to `bronze/assets/{page_id}-{filename}`; 300/300 physical files found.
- Independently recomputed SHA-1 and byte size against `bronze/manifests/assets.json`.
- Visually reviewed 12 contact sheets of 25 assets each. PNG/JPEG/GIF files were decoded; SVG files were rasterized for visual review. All 300 rendered successfully.
- Visual assessment is thumbnail-scale QA. It does not establish historical authenticity, cartographic accuracy, copyright provenance, or intended canon.

### Verification results
| Result | Count |
|---|---:|
| Physical files mapped | 300 / 300 |
| SHA-1 and size exact matches | 288 |
| SHA-1 and size mismatches | 12 |
| Missing physical files | 0 |
| Decode/parse failures | 0 |
| Visually reviewed | 300 / 300 |

Format distribution: 269 PNG, 14 SVG, 12 JPG, 3 GIF, 1 JPEG, and 1 extensionless raster image. All were successfully decoded or parsed.

### Mismatch register
Archive SHA-1 and byte size:

| Index | Page ID | Asset | Manifest bytes | Archive bytes | Archive SHA-1 |
|---:|---:|---|---:|---:|---|
| 303 | 1258 | Arch of Reunification.jpg | 315158 | 305779 | `0d260f151a46fc6e97613ad3a7b7a6f72752a185` |
| 304 | 1259 | DMZ.jpg | 442870 | 415643 | `4352dc8a1c566eb50c032dd9fca93003524d51a2` |
| 307 | 1313 | Cory Booker.jpg | 108627 | 108609 | `5463c3d07743bc7a5085b26e159c240c907b416f` |
| 308 | 1338 | Atlas from boston dynamics.jpg | 50391 | 50373 | `114284ab0a1ab5b69216395fb95277999383ae78` |
| 331 | 1517 | Mindanao state flag.jpeg | 8368 | 8226 | `a2aa12667e0e60862786b3e3f61d37c673a8e6ba` |
| 379 | 1840 | Assyrian Flag.jpg | 32602 | 32584 | `3401e557e6fdd5af2ff0602149a0f5bb8498f2a9` |
| 549 | 2374 | Kirsten Gillibrand, official portrait.jpg | 31410 | 31392 | `241361214ae1bc40f68ee82eed4d1d6254186485` |
| 550 | 2375 | John Hickenlooper.jpg | 194196 | 194101 | `fc02a50783f6eae45ada2a32c188af7d54dcc2f2` |
| 551 | 2376 | Kamala Harris official photo.jpg | 113178 | 113114 | `fb05522630684a27db254d4d34e4a8f2367c63e7` |
| 552 | 2377 | Tulsi Gabbard, official portrait.jpg | 63608 | 63590 | `46d10e840da8dad0616e5692fdb844046c7148a5` |
| 556 | 2389 | Guadalupe Victoria - 02.jpg | 184937 | 157400 | `ee461390c489f3888650eaab03db943e7710287e` |
| 567 | 2419 | Mars 2050.jpg | 933545 | 917709 | `9b7c83f13bf995f00eb6c13cbb1e1ef81b2d9e93` |

The 12 mismatches are:
- Index 303, Arch of Reunification.jpg: 9,379 bytes smaller than manifest.
- Index 304, DMZ.jpg: 27,227 bytes smaller.
- Indices 307–308, Cory Booker and Atlas: 18 bytes smaller each.
- Index 331, Mindanao state flag: 142 bytes smaller.
- Index 379, Assyrian Flag: 18 bytes smaller.
- Indices 549–552, four US political portraits: differences from 18 to 95 bytes.
- Index 556, Guadalupe Victoria portrait: 27,537 bytes smaller.
- Index 567, Mars 2050: 15,836 bytes smaller.

Several exact 18-byte deltas resemble the metadata-difference pattern noted in tranche 1. The larger deltas warrant provenance follow-up. None of these files failed to render or showed obvious corruption at contact-sheet scale. Do not alter the Bronze files or manifest hashes to force a match.

### Visual QA observations
- The tranche is dominated by political flags, state/national emblems, presidential portraits, demographic/economic charts, and maps of Korea, North America, Eurasia, the Moon, and Mars.
- Numerous black silhouette portraits are clearly generic placeholder artwork, not failed image loads.
- The sequence of US flags with different star counts appears to be intentional historical/worldbuilding reference material; verify the chronology against article text rather than treating the variants as duplicates.
- The maps and charts are legible at source scale; some dense maps and small charts are naturally difficult to assess from thumbnails.
- No obviously blank, truncated, or unreadable asset was identified.

### Progress
- Media manifest visually reviewed: 600 / 900 (66.67%).
- Physical files mapped: 600 / 899.
- Cumulative exact SHA-1/size matches: 531.
- Cumulative hash/size discrepancies: 69.
- Missing physical files: 0 in tranches 1 and 2. The known failed record, page ID 3525 (`File:K8ch1z55ucnz.png`), remains outside these batches.
- Remaining tranche: manifest entries 601–900.
