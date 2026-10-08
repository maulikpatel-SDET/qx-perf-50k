"""Service module 12179: business logic, no crypto."""


def calculate_total_12179(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12179():
    return 'module 12179 handles orders and invoices'
