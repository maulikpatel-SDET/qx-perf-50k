"""Service module 12024: business logic, no crypto."""


def calculate_total_12024(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12024():
    return 'module 12024 handles orders and invoices'
