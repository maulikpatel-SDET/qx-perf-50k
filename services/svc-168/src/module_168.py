"""Service module 168: business logic, no crypto."""


def calculate_total_168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_168():
    return 'module 168 handles orders and invoices'
