"""Service module 20127: business logic, no crypto."""


def calculate_total_20127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20127():
    return 'module 20127 handles orders and invoices'
