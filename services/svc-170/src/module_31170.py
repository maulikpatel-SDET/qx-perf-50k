"""Service module 31170: business logic, no crypto."""


def calculate_total_31170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31170():
    return 'module 31170 handles orders and invoices'
