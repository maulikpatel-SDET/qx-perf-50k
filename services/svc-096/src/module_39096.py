"""Service module 39096: business logic, no crypto."""


def calculate_total_39096(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39096():
    return 'module 39096 handles orders and invoices'
