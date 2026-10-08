"""Service module 41713: business logic, no crypto."""


def calculate_total_41713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41713():
    return 'module 41713 handles orders and invoices'
