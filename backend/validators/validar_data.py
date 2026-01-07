from datetime import datetime


def formatar_data_sqlite(data_str):
    if not data_str or data_str.lower() == "none":
        return None
    

    try:
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:

        try:
            return datetime.strptime(data_str, "%d/%m/%y").strftime("%d/%m/%Y")
        except ValueError:

            return data_str
