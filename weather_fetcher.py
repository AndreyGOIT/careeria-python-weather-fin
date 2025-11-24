# weather_fetcher.py
from fmiopendata.wfs import download_stored_query
from datetime import datetime, timedelta

def hae_lampotila(paikkakunta: str):
    # time range: last hour
    end = datetime.utcnow()
    start = end - timedelta(hours=1)
    args = [
        f"place={paikkakunta}",
        f"starttime={start.isoformat(timespec='seconds')}Z",
        f"endtime={end.isoformat(timespec='seconds')}Z"
    ]

    try:
        data = download_stored_query("fmi::observations::weather::multipointcoverage", args=args)
        raw = data.data

        if not isinstance(raw, dict):
            return None

        for timestep, stations in raw.items():
            if not isinstance(stations, dict):
                continue

            for station_name, params in stations.items():
                if "Air temperature" in params:
                    val = params["Air temperature"]["value"]
                    try:
                        return float(val)
                    except (TypeError, ValueError):
                        continue
        return None
    except Exception:
        return None

# Example usage:
# temp = hae_lampotila("Helsinki")
# print(f"Lämpötila Helsingissä: {temp} °C" if temp is not None else "Lämpötilaa ei löytynyt.")