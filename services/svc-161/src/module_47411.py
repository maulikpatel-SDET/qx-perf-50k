"""Service module 47411: business logic, no crypto."""


def calculate_total_47411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47411():
    return 'module 47411 handles orders and invoices'
