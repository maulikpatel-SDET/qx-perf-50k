"""Service module 13581: business logic, no crypto."""


def calculate_total_13581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13581():
    return 'module 13581 handles orders and invoices'
