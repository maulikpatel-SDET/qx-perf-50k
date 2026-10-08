"""Service module 36411: business logic, no crypto."""


def calculate_total_36411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36411():
    return 'module 36411 handles orders and invoices'
