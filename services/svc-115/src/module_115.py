"""Service module 115: business logic, no crypto."""


def calculate_total_115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_115():
    return 'module 115 handles orders and invoices'
