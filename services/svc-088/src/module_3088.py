"""Service module 3088: business logic, no crypto."""


def calculate_total_3088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3088():
    return 'module 3088 handles orders and invoices'
