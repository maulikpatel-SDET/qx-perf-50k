"""Service module 46983: business logic, no crypto."""


def calculate_total_46983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46983():
    return 'module 46983 handles orders and invoices'
