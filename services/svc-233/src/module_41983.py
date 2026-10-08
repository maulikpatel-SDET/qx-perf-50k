"""Service module 41983: business logic, no crypto."""


def calculate_total_41983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41983():
    return 'module 41983 handles orders and invoices'
