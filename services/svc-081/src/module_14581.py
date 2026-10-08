"""Service module 14581: business logic, no crypto."""


def calculate_total_14581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14581():
    return 'module 14581 handles orders and invoices'
