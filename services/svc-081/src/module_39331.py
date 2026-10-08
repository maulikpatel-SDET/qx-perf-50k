"""Service module 39331: business logic, no crypto."""


def calculate_total_39331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39331():
    return 'module 39331 handles orders and invoices'
