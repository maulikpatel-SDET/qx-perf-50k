"""Service module 35168: business logic, no crypto."""


def calculate_total_35168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35168():
    return 'module 35168 handles orders and invoices'
