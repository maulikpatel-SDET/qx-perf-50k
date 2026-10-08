"""Service module 47854: business logic, no crypto."""


def calculate_total_47854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47854():
    return 'module 47854 handles orders and invoices'
