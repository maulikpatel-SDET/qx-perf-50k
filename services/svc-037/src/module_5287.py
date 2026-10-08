"""Service module 5287: business logic, no crypto."""


def calculate_total_5287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5287():
    return 'module 5287 handles orders and invoices'
