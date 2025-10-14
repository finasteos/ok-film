from pipeline import mint_render
clip = mint_render(
    text="Kimi auntie says: Don't eat the blockchain, älskling.",
    voice="sv_nora_mint",
    music="lofi_modem",
    style="greyscale_accent_mint"
)
clip.export("clip01.mp4")