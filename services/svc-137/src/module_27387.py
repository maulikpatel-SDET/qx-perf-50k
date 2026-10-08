"""Service module 27387: business logic, no crypto."""


def calculate_total_27387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27387():
    return 'module 27387 handles orders and invoices'
