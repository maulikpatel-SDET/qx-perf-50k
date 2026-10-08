"""Service module 37581: business logic, no crypto."""


def calculate_total_37581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37581():
    return 'module 37581 handles orders and invoices'
