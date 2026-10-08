"""Service module 39036: business logic, no crypto."""


def calculate_total_39036(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39036():
    return 'module 39036 handles orders and invoices'
