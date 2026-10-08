"""Service module 5170: business logic, no crypto."""


def calculate_total_5170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5170():
    return 'module 5170 handles orders and invoices'
