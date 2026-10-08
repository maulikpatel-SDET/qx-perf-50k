"""Service module 13291: business logic, no crypto."""


def calculate_total_13291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13291():
    return 'module 13291 handles orders and invoices'
