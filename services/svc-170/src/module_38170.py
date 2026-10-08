"""Service module 38170: business logic, no crypto."""


def calculate_total_38170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38170():
    return 'module 38170 handles orders and invoices'
