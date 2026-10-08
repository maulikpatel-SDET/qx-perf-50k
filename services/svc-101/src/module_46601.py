"""Service module 46601: business logic, no crypto."""


def calculate_total_46601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46601():
    return 'module 46601 handles orders and invoices'
