"""Service module 17983: business logic, no crypto."""


def calculate_total_17983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17983():
    return 'module 17983 handles orders and invoices'
