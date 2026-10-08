"""Service module 6962: business logic, no crypto."""


def calculate_total_6962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6962():
    return 'module 6962 handles orders and invoices'
