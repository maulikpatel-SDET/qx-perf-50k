"""Service module 4679: business logic, no crypto."""


def calculate_total_4679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4679():
    return 'module 4679 handles orders and invoices'
