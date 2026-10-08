"""Service module 6397: business logic, no crypto."""


def calculate_total_6397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6397():
    return 'module 6397 handles orders and invoices'
