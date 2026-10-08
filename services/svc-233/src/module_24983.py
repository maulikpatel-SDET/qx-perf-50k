"""Service module 24983: business logic, no crypto."""


def calculate_total_24983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24983():
    return 'module 24983 handles orders and invoices'
