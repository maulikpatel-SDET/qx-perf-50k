"""Service module 20741: business logic, no crypto."""


def calculate_total_20741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20741():
    return 'module 20741 handles orders and invoices'
