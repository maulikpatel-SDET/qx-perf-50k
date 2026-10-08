"""Service module 21964: business logic, no crypto."""


def calculate_total_21964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21964():
    return 'module 21964 handles orders and invoices'
