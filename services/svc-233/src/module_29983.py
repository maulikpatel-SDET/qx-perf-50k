"""Service module 29983: business logic, no crypto."""


def calculate_total_29983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29983():
    return 'module 29983 handles orders and invoices'
