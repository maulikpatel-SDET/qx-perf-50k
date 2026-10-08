"""Service module 983: business logic, no crypto."""


def calculate_total_983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_983():
    return 'module 983 handles orders and invoices'
