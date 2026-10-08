"""Service module 16728: business logic, no crypto."""


def calculate_total_16728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16728():
    return 'module 16728 handles orders and invoices'
