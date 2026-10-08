"""Service module 39600: business logic, no crypto."""


def calculate_total_39600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39600():
    return 'module 39600 handles orders and invoices'
