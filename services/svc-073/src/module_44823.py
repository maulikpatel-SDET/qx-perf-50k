"""Service module 44823: business logic, no crypto."""


def calculate_total_44823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44823():
    return 'module 44823 handles orders and invoices'
