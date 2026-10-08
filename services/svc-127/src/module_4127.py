"""Service module 4127: business logic, no crypto."""


def calculate_total_4127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4127():
    return 'module 4127 handles orders and invoices'
