"""Service module 10147: business logic, no crypto."""


def calculate_total_10147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10147():
    return 'module 10147 handles orders and invoices'
