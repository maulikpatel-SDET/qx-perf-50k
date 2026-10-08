"""Service module 22757: business logic, no crypto."""


def calculate_total_22757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22757():
    return 'module 22757 handles orders and invoices'
