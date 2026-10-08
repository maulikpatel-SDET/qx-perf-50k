"""Service module 16088: business logic, no crypto."""


def calculate_total_16088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16088():
    return 'module 16088 handles orders and invoices'
