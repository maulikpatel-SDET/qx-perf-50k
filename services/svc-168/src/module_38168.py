"""Service module 38168: business logic, no crypto."""


def calculate_total_38168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38168():
    return 'module 38168 handles orders and invoices'
