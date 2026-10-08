"""Service module 20757: business logic, no crypto."""


def calculate_total_20757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20757():
    return 'module 20757 handles orders and invoices'
