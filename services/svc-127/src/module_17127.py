"""Service module 17127: business logic, no crypto."""


def calculate_total_17127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17127():
    return 'module 17127 handles orders and invoices'
