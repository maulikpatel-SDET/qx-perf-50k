"""Service module 25575: business logic, no crypto."""


def calculate_total_25575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25575():
    return 'module 25575 handles orders and invoices'
