"""Service module 46731: business logic, no crypto."""


def calculate_total_46731(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46731():
    return 'module 46731 handles orders and invoices'
