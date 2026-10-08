"""Service module 25088: business logic, no crypto."""


def calculate_total_25088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25088():
    return 'module 25088 handles orders and invoices'
