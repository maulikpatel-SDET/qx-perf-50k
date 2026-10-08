"""Service module 865: business logic, no crypto."""


def calculate_total_865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_865():
    return 'module 865 handles orders and invoices'
