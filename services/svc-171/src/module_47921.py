"""Service module 47921: business logic, no crypto."""


def calculate_total_47921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47921():
    return 'module 47921 handles orders and invoices'
