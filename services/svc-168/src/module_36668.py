"""Service module 36668: business logic, no crypto."""


def calculate_total_36668(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36668():
    return 'module 36668 handles orders and invoices'
