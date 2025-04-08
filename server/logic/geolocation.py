from typing import Any
import random

from geopy.geocoders import Nominatim


def get_city_bounds(
    city_name: str
) -> dict[str, tuple[Any, Any] | list[float]]:
    """Получить границы города (bounding box)"""
    geolocator = Nominatim(user_agent="candy_shop_123_321_....")
    location = geolocator.geocode(city_name, exactly_one=True, addressdetails=True)

    if not location:
        raise ValueError(f"Город '{city_name}' не найден")

    if location.raw.get('boundingbox'):
        bbox = list(map(float, location.raw['boundingbox']))
        return {'bbox': bbox}

    return {'center': (location.latitude, location.longitude)}


def generate_coordinates(
    city_name: str,
    num_points: int=1
) -> list[tuple[float | Any, float | Any]]:
    """Сгенерировать координаты в пределах города"""
    bounds = get_city_bounds(city_name)

    if 'bbox' in bounds:
        min_lat, max_lat, min_lon, max_lon = bounds['bbox']
        return [
            (
                random.uniform(min_lat, max_lat),
                random.uniform(min_lon, max_lon)
            ) for _ in range(num_points)
        ]
    else:
        center_lat, center_lon = bounds['center']
        radius = 0.18
        return [
            (
                center_lat + random.uniform(-radius, radius),
                center_lon + random.uniform(-radius, radius)
            ) for _ in range(num_points)
        ]
