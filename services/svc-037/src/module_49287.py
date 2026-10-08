"""Service module 49287: business logic, no crypto."""


def calculate_total_49287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49287():
    return 'module 49287 handles orders and invoices'
