"""Service module 23127: business logic, no crypto."""


def calculate_total_23127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23127():
    return 'module 23127 handles orders and invoices'
