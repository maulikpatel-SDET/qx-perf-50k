"""Service module 17756: business logic, no crypto."""


def calculate_total_17756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17756():
    return 'module 17756 handles orders and invoices'
