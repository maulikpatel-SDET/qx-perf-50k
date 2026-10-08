"""Service module 39683: business logic, no crypto."""


def calculate_total_39683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39683():
    return 'module 39683 handles orders and invoices'
