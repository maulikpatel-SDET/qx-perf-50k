"""Service module 49372: business logic, no crypto."""


def calculate_total_49372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49372():
    return 'module 49372 handles orders and invoices'
