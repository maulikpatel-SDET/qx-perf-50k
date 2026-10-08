"""Service module 15725: business logic, no crypto."""


def calculate_total_15725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15725():
    return 'module 15725 handles orders and invoices'
