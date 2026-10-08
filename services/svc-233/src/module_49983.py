"""Service module 49983: business logic, no crypto."""


def calculate_total_49983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49983():
    return 'module 49983 handles orders and invoices'
