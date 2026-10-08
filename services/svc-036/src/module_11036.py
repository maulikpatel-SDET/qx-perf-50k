"""Service module 11036: business logic, no crypto."""


def calculate_total_11036(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11036():
    return 'module 11036 handles orders and invoices'
