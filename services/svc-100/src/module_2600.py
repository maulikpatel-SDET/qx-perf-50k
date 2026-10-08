"""Service module 2600: business logic, no crypto."""


def calculate_total_2600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2600():
    return 'module 2600 handles orders and invoices'
