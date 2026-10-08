"""Service module 45100: business logic, no crypto."""


def calculate_total_45100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45100():
    return 'module 45100 handles orders and invoices'
