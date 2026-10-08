"""Service module 24029: business logic, no crypto."""


def calculate_total_24029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24029():
    return 'module 24029 handles orders and invoices'
