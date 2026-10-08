"""Service module 21668: business logic, no crypto."""


def calculate_total_21668(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21668():
    return 'module 21668 handles orders and invoices'
