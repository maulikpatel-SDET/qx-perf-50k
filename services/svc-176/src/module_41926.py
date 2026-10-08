"""Service module 41926: business logic, no crypto."""


def calculate_total_41926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41926():
    return 'module 41926 handles orders and invoices'
