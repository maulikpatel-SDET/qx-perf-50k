"""Service module 6168: business logic, no crypto."""


def calculate_total_6168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6168():
    return 'module 6168 handles orders and invoices'
