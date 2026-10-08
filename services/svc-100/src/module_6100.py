"""Service module 6100: business logic, no crypto."""


def calculate_total_6100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6100():
    return 'module 6100 handles orders and invoices'
