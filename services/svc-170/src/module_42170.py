"""Service module 42170: business logic, no crypto."""


def calculate_total_42170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42170():
    return 'module 42170 handles orders and invoices'
