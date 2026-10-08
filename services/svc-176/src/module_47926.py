"""Service module 47926: business logic, no crypto."""


def calculate_total_47926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47926():
    return 'module 47926 handles orders and invoices'
