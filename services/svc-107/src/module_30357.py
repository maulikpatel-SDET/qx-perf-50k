"""Service module 30357: business logic, no crypto."""


def calculate_total_30357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30357():
    return 'module 30357 handles orders and invoices'
