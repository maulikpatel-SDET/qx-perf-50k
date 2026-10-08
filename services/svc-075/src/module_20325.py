"""Service module 20325: business logic, no crypto."""


def calculate_total_20325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20325():
    return 'module 20325 handles orders and invoices'
