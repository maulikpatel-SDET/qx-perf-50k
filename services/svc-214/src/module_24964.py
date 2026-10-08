"""Service module 24964: business logic, no crypto."""


def calculate_total_24964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24964():
    return 'module 24964 handles orders and invoices'
