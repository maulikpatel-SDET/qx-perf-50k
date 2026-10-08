"""Service module 48674: business logic, no crypto."""


def calculate_total_48674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48674():
    return 'module 48674 handles orders and invoices'
