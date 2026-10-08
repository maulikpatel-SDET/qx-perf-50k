"""Service module 33723: business logic, no crypto."""


def calculate_total_33723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33723():
    return 'module 33723 handles orders and invoices'
