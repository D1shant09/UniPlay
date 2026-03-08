from textual.theme import Theme

THEMES = [
    Theme(name="matrix",           primary="#00ff41", background="#0d0d0d", surface="#111111", panel="#1a3a1a", accent="#00cc33",  foreground="#ccffcc", dark=True),
    Theme(name="amber",            primary="#ffb000", background="#100800", surface="#1a1000", panel="#2a1f00", accent="#ff8800",  foreground="#ffe4aa", dark=True),
    Theme(name="ocean",            primary="#00d4ff", background="#001520", surface="#001f2e", panel="#002f45", accent="#0099cc",  foreground="#aaeeff", dark=True),
    Theme(name="dracula",          primary="#bd93f9", background="#282a36", surface="#1e1f29", panel="#3a3a5c", accent="#ff79c6",  foreground="#f8f8f2", dark=True),
    Theme(name="mono",             primary="#e0e0e0", background="#141414", surface="#1e1e1e", panel="#2e2e2e", accent="#888888",  foreground="#cccccc", dark=True),
    Theme(name="tokyo-night",      primary="#7aa2f7", background="#1a1b2e", surface="#1f2335", panel="#292e42", accent="#9ece6a",  foreground="#cfc9c2", dark=True),
    Theme(name="gruvbox",          primary="#d4be98", background="#282828", surface="#3c3836", panel="#504945", accent="#a9b665",  foreground="#d4be98", dark=True),
    Theme(name="catppuccin",       primary="#89b4fa", background="#1e1e2e", surface="#313244", panel="#45475a", accent="#a6e3a1",  foreground="#cdd6f4", dark=True),
    Theme(name="nord",             primary="#81a1c1", background="#2e3440", surface="#3b4252", panel="#434c5e", accent="#a3be8c",  foreground="#d8dee9", dark=True),
    Theme(name="rose-pine",        primary="#c4a7e7", background="#191724", surface="#1f1d2e", panel="#2a2837", accent="#9ccfd8",  foreground="#e0def4", dark=True),
    Theme(name="everforest",       primary="#a7c080", background="#2d353b", surface="#343f44", panel="#3d484d", accent="#7fbbb3",  foreground="#d3c6aa", dark=True),
    Theme(name="kanagawa",         primary="#7e9cd8", background="#1f1f28", surface="#2a2a37", panel="#363646", accent="#76946a",  foreground="#dcd7ba", dark=True),
    Theme(name="ayu-mirage",       primary="#73d0ff", background="#1f2430", surface="#242936", panel="#2e3440", accent="#d5ff80",  foreground="#f3f4f5", dark=True),
    Theme(name="hackerman",        primary="#82fb9c", background="#0a0f0a", surface="#111511", panel="#162016", accent="#50f7d4",  foreground="#ddf7ff", dark=True),
    Theme(name="osaka-jade",       primary="#509475", background="#0d1a12", surface="#162312", panel="#1f2e1a", accent="#549e6a",  foreground="#f7e8b2", dark=True),
    Theme(name="matte-black",      primary="#e68e0d", background="#0a0a0a", surface="#141414", panel="#1e1e1e", accent="#ffc107",  foreground="#bebebe", dark=True),
    Theme(name="vantablack",       primary="#ffffff", background="#000000", surface="#0a0a0a", panel="#141414", accent="#8d8d8d",  foreground="#ffffff", dark=True),
    Theme(name="miasma",           primary="#78824b", background="#1a1a15", surface="#222218", panel="#2a2a20", accent="#5f875f",  foreground="#c2c2b0", dark=True),
    Theme(name="ristretto",        primary="#f38d70", background="#1a0f0f", surface="#231414", panel="#2e1c1c", accent="#adda78",  foreground="#e6d9db", dark=True),
    Theme(name="ethereal",         primary="#7d82d9", background="#1a1a2e", surface="#232340", panel="#2e2e52", accent="#92a593",  foreground="#ffcead", dark=True),
    Theme(name="catppuccin-latte", primary="#1e66f5", background="#eff1f5", surface="#e6e9ef", panel="#dce0e8", accent="#40a02b",  foreground="#4c4f69", dark=False),
    Theme(name="flexoki-light",    primary="#205ea6", background="#fffcf0", surface="#f2f0e5", panel="#e6e4d9", accent="#879a39",  foreground="#100f0f", dark=False),
]

THEME_NAMES = [t.name for t in THEMES]
DEFAULT_THEME = "matrix"
