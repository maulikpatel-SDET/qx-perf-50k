"""Service module 8100: business logic, no crypto."""


def calculate_total_8100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8100():
    return 'module 8100 handles orders and invoices'
