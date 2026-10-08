"""Service module 28908: business logic, no crypto."""


def calculate_total_28908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28908():
    return 'module 28908 handles orders and invoices'
