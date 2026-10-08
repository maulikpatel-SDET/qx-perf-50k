"""Service module 2287: business logic, no crypto."""


def calculate_total_2287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2287():
    return 'module 2287 handles orders and invoices'
