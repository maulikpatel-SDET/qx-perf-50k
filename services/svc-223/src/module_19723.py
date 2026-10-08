"""Service module 19723: business logic, no crypto."""


def calculate_total_19723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19723():
    return 'module 19723 handles orders and invoices'
