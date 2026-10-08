"""Service module 37926: business logic, no crypto."""


def calculate_total_37926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37926():
    return 'module 37926 handles orders and invoices'
