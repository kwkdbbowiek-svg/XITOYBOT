import os
from dotenv import load_dotenv

load_dotenv()

# ── Bot token ─────────────────────────────────────────────────
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

# ── Database ──────────────────────────────────────────────────
# Railway da PostgreSQL plugin qo'shilsa DATABASE_URL o'zi beriladi.
# Lokal uchun SQLite ishlatiladi.
_raw_db = os.getenv("DATABASE_URL", "")

# Agar DATABASE_URL yo'q bo'lsa, alohida parametrlardan yaratamiz
if not _raw_db:
    # Railway PostgreSQL o'zgaruvchilaridan DATABASE_URL yasaymiz
    pg_host = os.getenv("PGHOST", "")
    pg_port = os.getenv("PGPORT", "5432")
    pg_user = os.getenv("PGUSER", "")
    pg_password = os.getenv("PGPASSWORD", "")
    pg_database = os.getenv("PGDATABASE", "")
    
    if pg_host and pg_user and pg_password and pg_database:
        # Public host ishlatamiz (railway.internal o'rniga)
        if "railway.internal" in pg_host:
            # Railway public URL ni topishga harakat qilamiz
            public_url = os.getenv("DATABASE_PUBLIC_URL", "")
            if public_url:
                _raw_db = public_url
            else:
                print("⚠️  OGOHLANTIRISH: Private network ishlamayapti!")
                print("Railway dashboarddan DATABASE_PUBLIC_URL ni qo'shing")
                _raw_db = f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
        else:
            _raw_db = f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
    else:
        print("⚠️  OGOHLANTIRISH: DATABASE_URL topilmadi!")
        print("Railway da PostgreSQL qo'shing yoki .env faylida DATABASE_URL ni to'ldiring")
        _raw_db = "sqlite+aiosqlite:///bot.db"

# DATABASE_URL formatini to'g'rilaymiz
if _raw_db.startswith("postgres://"):
    _raw_db = _raw_db.replace("postgres://", "postgresql+asyncpg://", 1)
elif _raw_db.startswith("postgresql://") and "+asyncpg" not in _raw_db:
    _raw_db = _raw_db.replace("postgresql://", "postgresql+asyncpg://", 1)

DATABASE_URL: str = _raw_db
print(f"🔧 Database URL: {DATABASE_URL[:30]}..." if len(DATABASE_URL) > 30 else f"🔧 Database URL: {DATABASE_URL}")

# ── Admin IDlar ───────────────────────────────────────────────
_raw_ids = os.getenv("SUPER_ADMIN_IDS", "")
SUPER_ADMIN_IDS: list[int] = [
    int(i.strip()) for i in _raw_ids.split(",") if i.strip().isdigit()
]

# ── Webhook / Railway ────────────────────────────────────────
PORT: int = int(os.getenv("PORT", "8080"))

_raw_webhook_url = os.getenv("WEBHOOK_URL", "").strip()
if not _raw_webhook_url:
    railway_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN", "").strip()
    if not railway_domain:
        railway_domain = os.getenv("RAILWAY_STATIC_URL", "").strip()
    if railway_domain:
        _raw_webhook_url = f"https://{railway_domain}"

WEBHOOK_URL: str = _raw_webhook_url.rstrip("/")
WEBHOOK_PATH: str = os.getenv("WEBHOOK_PATH", "/webhook").strip()
WEBHOOK_SECRET: str = os.getenv("WEBHOOK_SECRET", "")

# ── Referal / Yechish ─────────────────────────────────────────
REFERRAL_BONUS: int = int(os.getenv("REFERRAL_BONUS", "20000"))
MIN_WITHDRAWAL: int = int(os.getenv("MIN_WITHDRAWAL", "50000"))

# ── Cheklar kanali ────────────────────────────────────────────
_rcid = os.getenv("RECEIPTS_CHANNEL_ID", "").strip()
RECEIPTS_CHANNEL_ID: int | None = int(_rcid) if _rcid.lstrip("-").isdigit() else None

