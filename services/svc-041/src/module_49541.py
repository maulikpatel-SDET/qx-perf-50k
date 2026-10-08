"""Service module 49541: business logic, no crypto."""


def calculate_total_49541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49541():
    return 'module 49541 handles orders and invoices'
