"""Service module 19242: business logic, no crypto."""


def calculate_total_19242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19242():
    return 'module 19242 handles orders and invoices'
