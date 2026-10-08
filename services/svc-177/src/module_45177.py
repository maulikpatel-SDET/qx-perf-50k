"""Service module 45177: business logic, no crypto."""


def calculate_total_45177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45177():
    return 'module 45177 handles orders and invoices'
