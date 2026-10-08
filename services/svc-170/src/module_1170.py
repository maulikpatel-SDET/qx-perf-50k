"""Service module 1170: business logic, no crypto."""


def calculate_total_1170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1170():
    return 'module 1170 handles orders and invoices'
