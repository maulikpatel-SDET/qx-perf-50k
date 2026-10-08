"""Service module 25815: business logic, no crypto."""


def calculate_total_25815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25815():
    return 'module 25815 handles orders and invoices'
