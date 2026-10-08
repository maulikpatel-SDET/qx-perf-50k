"""Service module 32356: business logic, no crypto."""


def calculate_total_32356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32356():
    return 'module 32356 handles orders and invoices'
