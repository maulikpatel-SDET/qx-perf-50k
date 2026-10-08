"""Service module 47581: business logic, no crypto."""


def calculate_total_47581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47581():
    return 'module 47581 handles orders and invoices'
