"""Service module 344: business logic, no crypto."""


def calculate_total_344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_344():
    return 'module 344 handles orders and invoices'
