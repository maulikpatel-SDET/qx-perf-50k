"""Service module 25668: business logic, no crypto."""


def calculate_total_25668(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25668():
    return 'module 25668 handles orders and invoices'
