"""Service module 39597: business logic, no crypto."""


def calculate_total_39597(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39597():
    return 'module 39597 handles orders and invoices'
