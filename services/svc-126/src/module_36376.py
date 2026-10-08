"""Service module 36376: business logic, no crypto."""


def calculate_total_36376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36376():
    return 'module 36376 handles orders and invoices'
