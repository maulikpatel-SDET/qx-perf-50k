"""Service module 10139: business logic, no crypto."""


def calculate_total_10139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10139():
    return 'module 10139 handles orders and invoices'
