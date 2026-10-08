"""Service module 8387: business logic, no crypto."""


def calculate_total_8387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8387():
    return 'module 8387 handles orders and invoices'
