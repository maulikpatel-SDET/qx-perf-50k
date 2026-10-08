"""Service module 3926: business logic, no crypto."""


def calculate_total_3926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3926():
    return 'module 3926 handles orders and invoices'
