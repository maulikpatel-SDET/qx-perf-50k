"""Service module 8424: business logic, no crypto."""


def calculate_total_8424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8424():
    return 'module 8424 handles orders and invoices'
