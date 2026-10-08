"""Service module 23668: business logic, no crypto."""


def calculate_total_23668(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23668():
    return 'module 23668 handles orders and invoices'
