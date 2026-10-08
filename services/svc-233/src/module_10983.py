"""Service module 10983: business logic, no crypto."""


def calculate_total_10983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10983():
    return 'module 10983 handles orders and invoices'
