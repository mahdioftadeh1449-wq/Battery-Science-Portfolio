import os
from pathlib import Path
from dotenv import load_dotenv
from mp_api.client import MPRester

# تعیین مسیرها به صورت داینامیک
CURRENT_PROJECT_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = CURRENT_PROJECT_DIR.parent

# لود کردن کلید از فایل .env موجود در ریشه مخزن
load_dotenv(dotenv_path=REPO_ROOT / ".env")
api_key = os.getenv("MP_API_KEY")

if not api_key:
    raise ValueError("❌ خطا: کلید MP_API_KEY در فایل .env یافت نشد!")

def fetch_nasicon_baseline():
    print("⏳ در حال اتصال به Materials Project...")
    with MPRester(api_key) as mpr:
        # mp-20371 شناسه استاندارد کاتد Na3V2(PO4)3 است
        structure = mpr.get_structure_by_material_id("mp-20371")
        
        output_dir = CURRENT_PROJECT_DIR / "data" / "raw"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "Na3V2(PO4)3_baseline.cif"
        
        structure.to(filename=str(output_path))
        
        print("\n" + "="*50)
        print("✅ موفقیت! ساختار مرجع NASICON دانلود و ذخیره شد:")
        print(f"📁 مسیر فایل: {output_path}")
        print(f"⚛️ تعداد کل اتم‌ها: {len(structure)}")
        print(f"🧪 فرمول شیمیایی: {structure.composition.reduced_formula}")
        print("="*50)

if __name__ == "__main__":
    fetch_nasicon_baseline()
