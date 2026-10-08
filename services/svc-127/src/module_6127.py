"""Service module 6127: business logic, no crypto."""


def calculate_total_6127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6127():
    return 'module 6127 handles orders and invoices'
