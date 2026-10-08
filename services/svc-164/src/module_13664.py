"""Service module 13664: business logic, no crypto."""


def calculate_total_13664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13664():
    return 'module 13664 handles orders and invoices'
