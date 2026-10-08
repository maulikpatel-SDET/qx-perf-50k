"""Service module 34600: business logic, no crypto."""


def calculate_total_34600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34600():
    return 'module 34600 handles orders and invoices'
