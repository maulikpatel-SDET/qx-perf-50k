"""Service module 26964: business logic, no crypto."""


def calculate_total_26964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26964():
    return 'module 26964 handles orders and invoices'
