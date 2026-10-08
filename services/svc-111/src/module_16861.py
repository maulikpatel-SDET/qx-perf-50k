"""Service module 16861: business logic, no crypto."""


def calculate_total_16861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16861():
    return 'module 16861 handles orders and invoices'
