"""Service module 39483: business logic, no crypto."""


def calculate_total_39483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39483():
    return 'module 39483 handles orders and invoices'
