"""Service module 32517: business logic, no crypto."""


def calculate_total_32517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32517():
    return 'module 32517 handles orders and invoices'
