"""Service module 10662: business logic, no crypto."""


def calculate_total_10662(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10662():
    return 'module 10662 handles orders and invoices'
