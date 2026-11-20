# Media audit — manifest entries 1–300
## Completed 2026-11-20

### Scope and method
- Reviewed asset-manifest records 1–300 in original manifest order.
- Matched each record to the physical archive path `bronze/assets/{page_id}-{filename}`; all 300 records mapped to one physical file.
- Independently recomputed SHA-1 and byte size for each file against `bronze/manifests/assets.json`.
- Rendered and visually triaged all 300 assets in 12 contact sheets (25 assets per sheet), compositing transparency onto white and rasterizing SVGs for review. This is thumbnail-scale visual QA, not pixel-level forensic inspection or a claim that the source artwork is historically/geographically accurate.
- Validated decoding/parsing: 230 PNG, 55 JPEG, 13 SVG/XML, 1 ICO, and 1 GIF; zero decode/parse failures.

### Verification results
| Result | Count |
|---|---:|
| Physical files mapped | 300 / 300 |
| SHA-1 and size exact matches | 243 |
| SHA-1 and size mismatches | 57 |
| Missing physical files | 0 |
| Decode/parse failures | 0 |
| Visually reviewed | 300 / 300 |

The 57 mismatches are not all equivalent. Thirty-seven are exactly 18 bytes smaller than the manifest size, consistent with a small metadata/comment difference; the rest have larger byte deltas. All 57 files nevertheless decoded or parsed successfully and appeared visually coherent at contact-sheet scale. A mismatch is therefore a provenance/integrity discrepancy, not proof that the visual asset is corrupt or semantically wrong. Preserve the manifest values; do not rewrite the manifest or replace the Bronze bytes to make hashes agree.

### Mismatch register
The following entries differ from the manifest. Archive SHA-1 and byte size are shown for reproducibility.

| Index | Page ID | Title | Manifest bytes | Archive bytes | Archive SHA-1 |
|---:|---:|---|---:|---:|---|
| 9 | 117 | File:Blank Person.jpg | 17046 | 17028 | `9fbbfeaa5a5d5774b52694d8cddcf183d2f884df` |
| 28 | 238 | File:George-Washington.jpg | 11873 | 11766 | `c028dd0d8c95da90a6d8c2bb4cce5109a7faecb2` |
| 29 | 239 | File:US Navy 031029-N-6236G-001 A painting of President John Adams (1735-1826), 2nd president of the United States, by Asher B. Durand (1767-1845)-crop.jpg | 994930 | 994912 | `c726483b7b3823154b70601962680c7137eda81f` |
| 30 | 240 | File:Thomas Jefferson by Rembrandt Peale, 1800.jpg | 3084260 | 3084046 | `65c486158cb8ce44015598f9b078c87ecfe2d045` |
| 31 | 241 | File:James Madison.jpg | 2833088 | 2832874 | `96815f9ff76f21b9ad7b7072a24f10128b3d42d7` |
| 32 | 242 | File:Andrew Jackson Daguerrotype-crop.jpg | 2870303 | 2857429 | `050752a36202a6345cb03aab92de43c967fd94d8` |
| 33 | 243 | File:George-W-Bush.jpeg | 1936324 | 1921900 | `e9ff26d2134e5554dd19107025eed4bc52033048` |
| 34 | 244 | File:President Barack Obama.jpg | 1276121 | 1266784 | `6ace462624501ce6bdbf94ae12d5ac4360478bea` |
| 35 | 245 | File:Bill Clinton.jpg | 4470879 | 4440176 | `6e450004222a81af18cdb506af2fc02230087c3b` |
| 36 | 246 | File:George H. W. Bush, President of the United States, 1989 official portrait.jpg | 598271 | 598234 | `e536a9019795da5983941114f81b3e6f1c581b9e` |
| 37 | 247 | File:Official Portrait of President Reagan 1981.jpg | 1281250 | 1281232 | `b9b4d3221b7b455b4ad3cfa9f7dc9d4fc97f59d3` |
| 38 | 248 | File:Richard M. Nixon, ca. 1935 - 1982 - NARA - 530679.jpg | 1946345 | 1946327 | `f1ac63b9e6e7570793f26a60f76745fa6a37e5bf` |
| 40 | 250 | File:Dwight D. Eisenhower, White House photo portrait, February 1959.jpg | 1344483 | 1344465 | `704c104ff6239f6f89dc851d39b8354b18f00f1e` |
| 41 | 251 | File:Harry-truman.jpg | 43174 | 28890 | `09f5793f26da725a0b5e5acb34709bdeba1a4f16` |
| 42 | 252 | File:Franklin D. Roosevelt - NARA - 196715.jpg | 45236 | 45218 | `adddb4d0fef3c759f8030b485c9104834037e5e6` |
| 43 | 253 | File:HerbertHoover.jpg | 21466 | 21448 | `d2012dbcf4d496986e10c3bd85c3688c131c265c` |
| 44 | 254 | File:John Calvin Coolidge, Bain bw photo portrait.jpg | 44453 | 44435 | `5bd1d1f61784a73f284b46434bdc88011f5aa969` |
| 45 | 255 | File:Warren G Harding-Harris & Ewing.jpg | 25238 | 25220 | `a6f9c1bf53d7ca02d29af76ee809eb7dc61000b8` |
| 46 | 256 | File:President Woodrow Wilson portrait December 2 1912.jpg | 58174 | 58156 | `d1f7b3fddae533438ec041937e1fe668a64a2bcf` |
| 47 | 257 | File:William Howard Taft, Bain bw photo portrait, 1908.jpg | 30145 | 30127 | `3a3d24c7ec04be3780333034ac1e76149a376369` |
| 48 | 258 | File:President Theodore Roosevelt, 1904.jpg | 30393 | 30375 | `19af6da954587b363b0658eeba4d65115e00c37e` |
| 50 | 260 | File:Chester Alan Arthur.jpg | 37017 | 36999 | `c41bd91a91f18cc2c554bc7ab4c871810c3cb810` |
| 51 | 261 | File:James Abram Garfield, photo portrait seated.jpg | 27913 | 27895 | `ad1fea978a06fd69efc2ae4dc6c1b2bbe492c6a6` |
| 52 | 262 | File:President Rutherford Hayes 1870 - 1880.jpg | 38753 | 38735 | `6a934e63500e0eb0d05b5c2e46f936dfc3fbac05` |
| 54 | 264 | File:President Andrew Johnson.jpg | 45735 | 45717 | `28d030ba3e37bcafceb493b4d76be566c9f000e6` |
| 55 | 265 | File:Abraham Lincoln November 1863.jpg | 57082 | 57064 | `4b17cf3f8a2fb340318f057b3ff1c8f5324fc64d` |
| 56 | 266 | File:James Buchanan.jpg | 50458 | 50440 | `5e6fc72c6d4c2ffd8804a1398bd59e3abe0e0a4a` |
| 57 | 267 | File:Fillmore.jpg | 38082 | 38064 | `f3517c9cbaa18063b513c9128e05e6f029964b97` |
| 58 | 268 | File:Zachary Taylor-circa1850.jpg | 45506 | 45488 | `68ea0c4aaee598b307917d980841a41cf52aa7b5` |
| 59 | 269 | File:James K Polk.jpg | 41874 | 41856 | `ff454351ab124ac477422c4d9229355795f8d1be` |
| 60 | 270 | File:TylerDaguerreotype.jpg | 24328 | 24310 | `ac65d18bc6bcc32302b04148299d719d169a6075` |
| 61 | 271 | File:William Henry Harrison daguerreotype edit.jpg | 6340 | 6322 | `77abb2f732519060eacc949a6088ea0f27a35752` |
| 62 | 279 | File:John Quincy Adams daguerreotype c1840s.jpg | 15461 | 15443 | `1a359ea4dfe2e954e75dcf4fbc1f702ca2eefb8d` |
| 64 | 281 | File:Martin Van Buren by Mathew Brady c1855-58.jpg | 22737 | 22719 | `5cb16338abbc7500141565d07874e5afa5383d98` |
| 65 | 282 | File:Mathew Brady - Franklin Pierce - alternate crop.jpg | 57876 | 57858 | `f57a084bdf1be0c88976aa43379565fee0f2d9e5` |
| 66 | 283 | File:Pach Brothers - Benjamin Harrison.jpg | 36561 | 36543 | `647028332e81e61d0c535c77e396f368c85f9418` |
| 68 | 285 | File:Gerald Ford.jpg | 17471 | 17453 | `4d6cc2210b8ff5c405fc5d398c812729fa271fc3` |
| 69 | 286 | File:JimmyCarterPortrait.jpg | 17681 | 17663 | `e2ae31181cc18e2895abc8308f73a04ccd0f14ce` |
| 70 | 287 | File:Lyndon B. Johnson, photo portrait, leaning on chair, color.jpg | 28854 | 28836 | `544b1242274cd64438e4b51c7448bef5cfaf09d9` |
| 73 | 315 | File:Governor O'Malley Portrait.jpg | 331129 | 331017 | `7b5f26b48f8d0c6cef3278856ea5c2df01ecdbc4` |
| 176 | 504 | File:Bulgarian flag.jpg | 2653 | 2593 | `4637582cf3ac4933b1bf3c7cca475c2339a76bfb` |
| 177 | 505 | File:Flag of Austria.jpg | 8364 | 4082 | `138ab64e60e0fcf1fd2182fc30e991631ca00f79` |
| 194 | 536 | File:Flag of Saskatchewan.svg | 91735 | 90087 | `30e401190221b7c0d242c485a2c2f0cc957778aa` |
| 232 | 664 | File:Jeb Bush.jpg | 2975759 | 2961652 | `5b09bf1b0cf667005c1d5585aba153fc604e1233` |
| 233 | 665 | File:Donald Trump.jpg | 61617 | 61522 | `a6f80533404c9bc61845ed3325cd7b2ce0afab64` |
| 236 | 797 | File:John Kerry headshot with US flag.jpg | 298207 | 298189 | `63b68d504b2bff5ecdc2886b8fc6607ae0fec6eb` |
| 250 | 916 | File:United States Navy.jpg | 334395 | 325833 | `9c4563c921b143200da4df521247b3eb38393a5e` |
| 261 | 938 | File:Marco Rubio.jpg | 46272 | 46254 | `e222de1265191dd03048c12cf166ad13ceef5d94` |
| 274 | 1103 | File:Viking Flag.png | 117101 | 107265 | `b52369be49656eb2fc9f7c82c3ae267aadf95515` |
| 275 | 1112 | File:Hardiman.jpg | 147630 | 147612 | `f1ecb5ac0914546a55878bb83b6dbffe84374b82` |
| 276 | 1113 | File:Raytheon-exo2-clark-gregg-gazes.jpg | 122881 | 122844 | `97910f3caf542d2b505584fbbfdcbfda04eba2e6` |
| 290 | 1182 | File:Bernie Sanders.jpg | 282297 | 264407 | `bcf65c336c13910642044ee004d31fb3a62c9378` |
| 291 | 1183 | File:Ted Cruz.jpg | 38543 | 38525 | `9c3189c0e7ae49663a1308e34f101409ed1021c5` |
| 294 | 1228 | File:Governor John Kasich.jpg | 47165 | 47147 | `7bcf7e752e4858431b478281460b47c73fd67be9` |
| 295 | 1242 | File:BenSasse.jpg | 90250 | 90232 | `1d84e4a11893da2e5493f592df5777d08c7a2197` |
| 297 | 1244 | File:Blue Origin.jpg | 7482 | 7464 | `38ffb2a9167a0a56a92ec7dd62413e709faed6d8` |
| 299 | 1247 | File:Planet Labs.jpg | 42056 | 42019 | `38dede0eb2908cb13412792058fef0e102a0116a` |

### Visual QA observations
- The first 300 assets are dominated by historical/political maps, flags, presidential portraits, logos, insignia, and UI icons.
- No obviously truncated, blank, or unreadable asset was found in the 300 thumbnail review.
- Several tiny UI assets are intentionally minimal: `Increase2.png` is a small green upward marker, `Decrease.png` a red downward marker, and `11px-Steady2.png` a blue horizontal marker.
- Potential content-quality follow-ups, not confirmed defects: `Flag of Dubai.png` appears as a plain red field; `Flag of Patagonia.png` appears as a plain red/green bicolor; `Hispaniola.png` appears as four plain color quadrants. Confirm intended designs against page usage or source history before classifying them as errors.
- Transparent PNG banners and logos were reviewed against a white background; their initially black-looking thumbnails were a transparency-preview artifact, not black source images.
- SVG entries, including the Saskatchewan and Brazil flags, were parsed as XML and rendered for inspection.

### Progress
- Media records reviewed: 300 / 900 (33.33%).
- Physical files mapped: 300 / 899.
- Exact archive integrity matches: 243.
- Mapped hash/size discrepancies: 57.
- Known failed/missing manifest record remains outside this tranche: page ID 3525, `File:K8ch1z55ucnz.png`.
- Remaining work: manifest entries 301–600, then 601–900; after binary inspection, reconcile the one failed row and synthesize the full media QA report.
