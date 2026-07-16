"""
Configuration file for the RESOLVE Internship Analytics Portal.
"""

# =========================================================
# Application
# =========================================================

APP_NAME = "RESOLVE Internship Analytics Portal"

APP_ICON = "🪐"

APP_VERSION = "2.0"

# =========================================================
# Google Sheets
# =========================================================

SPREADSHEET_NAME = "RESOLVE INTERNS RECRUITMENT 2026"

CREDENTIALS_PATH = "secrets/credentials.json"

# =========================================================
# Internship
# =========================================================

INTERNSHIP_DURATION_WEEKS = 8

# =========================================================
# RESOLVE Brand Identity
# =========================================================

BRAND_NAME = "RESOLVE"

BRAND_SUBTITLE = "Research Solutions & Ventures (SUPARCO)"

PROGRAM_NAME = "Summer Internship Program 2026"

# =========================================================
# Official Brand Colors
# =========================================================

PRIMARY_BLUE = "#0F4C81"

PRIMARY_BLUE_DARK = "#083358"

PRIMARY_BLUE_LIGHT = "#D8EAF8"

PRIMARY_ORANGE = "#F58220"

PRIMARY_ORANGE_LIGHT = "#FFE8D6"

SUCCESS_GREEN = "#16A34A"

WARNING_YELLOW = "#EAB308"

ERROR_RED = "#DC2626"

INFO_BLUE = "#2563EB"

# =========================================================
# Background Palette
# =========================================================

PAGE_BACKGROUND = "#F4F7FB"

CARD_BACKGROUND = "#FFFFFF"

SIDEBAR_BACKGROUND = "#FFFFFF"

HEADER_BACKGROUND = "#FFFFFF"

SECTION_BACKGROUND = "#F8FAFC"

# =========================================================
# Text Palette
# =========================================================

TEXT_PRIMARY = "#1E293B"

TEXT_SECONDARY = "#64748B"

TEXT_MUTED = "#94A3B8"

TEXT_WHITE = "#FFFFFF"

# =========================================================
# Borders
# =========================================================

BORDER_COLOR = "#E2E8F0"

BORDER_LIGHT = "#F1F5F9"

BORDER_RADIUS_SMALL = "8px"

BORDER_RADIUS = "14px"

BORDER_RADIUS_LARGE = "20px"

# =========================================================
# Shadows
# =========================================================

CARD_SHADOW = (
    "0 4px 16px rgba(15,76,129,0.08)"
)

CARD_SHADOW_HOVER = (
    "0 14px 36px rgba(15,76,129,0.18)"
)

HEADER_SHADOW = (
    "0 3px 14px rgba(0,0,0,0.05)"
)

# =========================================================
# Sidebar
# =========================================================

SIDEBAR_WIDTH = "300px"

SIDEBAR_ACTIVE_COLOR = PRIMARY_BLUE

SIDEBAR_HOVER_COLOR = "#EAF4FC"

SIDEBAR_TEXT_COLOR = TEXT_PRIMARY

SIDEBAR_ACTIVE_TEXT = "#FFFFFF"

# =========================================================
# Buttons
# =========================================================

BUTTON_RADIUS = "10px"

BUTTON_HEIGHT = "46px"

BUTTON_PRIMARY = PRIMARY_BLUE

BUTTON_PRIMARY_HOVER = PRIMARY_BLUE_DARK

# =========================================================
# KPI Cards
# =========================================================

KPI_CARD_HEIGHT = "150px"

KPI_ICON_SIZE = "34px"

KPI_VALUE_SIZE = "36px"

KPI_TITLE_SIZE = "15px"

# =========================================================
# Header
# =========================================================

HEADER_HEIGHT = "170px"

LOGO_HEIGHT = "72px"

TITLE_SIZE = "44px"

SUBTITLE_SIZE = "17px"

# =========================================================
# Tables
# =========================================================

TABLE_ROW_HEIGHT = 46

TABLE_HEADER_COLOR = PRIMARY_BLUE

TABLE_BORDER = BORDER_COLOR

# =========================================================
# Charts
# =========================================================

CHART_HEIGHT = 470

CHART_TEMPLATE = "plotly_white"

GRID_COLOR = "#EDF2F7"

# =========================================================
# Layout
# =========================================================

CONTENT_MAX_WIDTH = "1600px"

SECTION_SPACING = "2.2rem"

CARD_GAP = "1.4rem"

PAGE_PADDING = "2rem"

# =========================================================
# Animation
# =========================================================

TRANSITION = "all .30s ease"

HOVER_SCALE = "1.02"
