"""Service module 47100: business logic, no crypto."""


def calculate_total_47100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47100():
    return 'module 47100 handles orders and invoices'
