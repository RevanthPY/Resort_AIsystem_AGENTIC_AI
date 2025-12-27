import pandas as pd
from sqlalchemy.orm import sessionmaker
from database import engine, MenuItem

def import_menu_from_excel():
    file_path = "Restaurant_Menu.xlsx"
    
    try:
        xl = pd.ExcelFile(file_path)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(MenuItem).delete()
        
        total_items = 0

        for sheet_name in xl.sheet_names:
            print(f"--- Processing: {sheet_name} ---")
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            
            # This creates a map that can find columns even with symbols or spaces
            col_map = {str(c).lower().strip(): c for c in df.columns}

            for _, row in df.iterrows():
                # 1. Look for 'item name' (matches your Column A)
                name_key = next((col_map[k] for k in ['item name', 'name', 'item'] if k in col_map), None)
                # 2. Look for 'price (₹)' (matches your Column C)
                price_key = next((col_map[k] for k in ['price (₹)', 'price', 'rate'] if k in col_map), None)
                # 3. Look for 'description' (matches your Column B)
                desc_key = next((col_map[k] for k in ['description', 'desc'] if k in col_map), None)

                item_name = row.get(name_key)
                
                if pd.isna(item_name) or str(item_name).strip() == "":
                    continue

                try:
                    new_item = MenuItem(
                        name=str(item_name).strip(),
                        description=str(row.get(desc_key, 'Freshly prepared')),
                        price=float(row.get(price_key, 0.0)),
                        category=sheet_name
                    )
                    session.add(new_item)
                    total_items += 1
                except Exception as row_err:
                    print(f"Skipping {item_name}: {row_err}")

        session.commit()
        print(f"\nSUCCESS: {total_items} items (like {item_name}) imported successfully!")
        session.close()

    except Exception as e:
        print(f"SYSTEM ERROR: {e}")

if __name__ == "__main__":
    import_menu_from_excel()