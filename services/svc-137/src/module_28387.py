"""Service module 28387: business logic, no crypto."""


def calculate_total_28387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28387():
    return 'module 28387 handles orders and invoices'
