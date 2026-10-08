"""Service module 23581: business logic, no crypto."""


def calculate_total_23581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23581():
    return 'module 23581 handles orders and invoices'
