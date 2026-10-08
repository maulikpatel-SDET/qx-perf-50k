"""Service module 28411: business logic, no crypto."""


def calculate_total_28411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28411():
    return 'module 28411 handles orders and invoices'
