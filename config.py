"""
Configuration file for the RESOLVE Internship Analytics Portal.
"""

# -----------------------------
# Application
# -----------------------------

APP_NAME = "RESOLVE Internship Analytics Portal"

APP_ICON = "🪐"

# -----------------------------
# Google Sheets
# -----------------------------

SPREADSHEET_NAME = "RESOLVE INTERNS RECRUITMENT 2026"

CREDENTIALS_PATH = "secrets/credentials.json"

# -----------------------------
# Internship Settings
# -----------------------------

INTERNSHIP_DURATION_WEEKS = 8

# ---------------------------------------------------------
# RESOLVE Design Theme
# ---------------------------------------------------------

# =========================================================
# Brand Colors
# =========================================================

PRIMARY_BLUE = "#1565C0"
PRIMARY_ORANGE = "#FF5A1F"

SUCCESS_GREEN = "#2E7D32"
WARNING_YELLOW = "#F9A825"
ERROR_RED = "#D32F2F"

# =========================================================
# Background Colors
# =========================================================

PAGE_BACKGROUND = "#FFFFFF"

CARD_BACKGROUND = "#FFFFFF"

SIDEBAR_BACKGROUND = "#FFFFFF"

HEADER_BACKGROUND = "#FFFFFF"

# =========================================================
# Text Colors
# =========================================================

TEXT_PRIMARY = "#1F2937"

TEXT_SECONDARY = "#6B7280"

TEXT_LIGHT = "#9CA3AF"

# =========================================================
# Borders
# =========================================================

BORDER_COLOR = "#E5E7EB"

BORDER_RADIUS = "12px"

# =========================================================
# Shadows
# =========================================================

CARD_SHADOW = (
    "0 8px 30px rgba(0,0,0,0.06)"
)

CARD_SHADOW_HOVER = (
    "0 16px 40px rgba(0,0,0,0.10)"
)

# =========================================================
# Layout
# =========================================================

CONTENT_MAX_WIDTH = "1400px"

HEADER_HEIGHT = "180px"

KPI_CARD_HEIGHT = "170px"

SECTION_SPACING = "2rem"