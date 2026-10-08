"""Service module 17397: business logic, no crypto."""


def calculate_total_17397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17397():
    return 'module 17397 handles orders and invoices'
