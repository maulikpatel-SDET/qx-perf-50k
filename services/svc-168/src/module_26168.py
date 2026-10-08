"""Service module 26168: business logic, no crypto."""


def calculate_total_26168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26168():
    return 'module 26168 handles orders and invoices'
