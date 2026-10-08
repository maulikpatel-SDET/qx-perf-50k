"""Service module 22127: business logic, no crypto."""


def calculate_total_22127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22127():
    return 'module 22127 handles orders and invoices'
