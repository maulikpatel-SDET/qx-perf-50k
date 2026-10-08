"""Service module 26983: business logic, no crypto."""


def calculate_total_26983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26983():
    return 'module 26983 handles orders and invoices'
