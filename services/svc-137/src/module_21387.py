"""Service module 21387: business logic, no crypto."""


def calculate_total_21387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21387():
    return 'module 21387 handles orders and invoices'
