"""Service module 41127: business logic, no crypto."""


def calculate_total_41127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41127():
    return 'module 41127 handles orders and invoices'
