"""Service module 34621: business logic, no crypto."""


def calculate_total_34621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34621():
    return 'module 34621 handles orders and invoices'
