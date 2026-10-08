"""Service module 14388: business logic, no crypto."""


def calculate_total_14388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14388():
    return 'module 14388 handles orders and invoices'
