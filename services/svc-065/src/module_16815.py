"""Service module 16815: business logic, no crypto."""


def calculate_total_16815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16815():
    return 'module 16815 handles orders and invoices'
