"""Service module 10397: business logic, no crypto."""


def calculate_total_10397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10397():
    return 'module 10397 handles orders and invoices'
