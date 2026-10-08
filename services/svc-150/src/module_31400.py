"""Service module 31400: business logic, no crypto."""


def calculate_total_31400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31400():
    return 'module 31400 handles orders and invoices'
