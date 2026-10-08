"""Service module 12600: business logic, no crypto."""


def calculate_total_12600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12600():
    return 'module 12600 handles orders and invoices'
