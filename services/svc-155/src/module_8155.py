"""Service module 8155: business logic, no crypto."""


def calculate_total_8155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8155():
    return 'module 8155 handles orders and invoices'
