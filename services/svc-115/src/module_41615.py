"""Service module 41615: business logic, no crypto."""


def calculate_total_41615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41615():
    return 'module 41615 handles orders and invoices'
