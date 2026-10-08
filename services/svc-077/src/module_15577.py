"""Service module 15577: business logic, no crypto."""


def calculate_total_15577(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15577():
    return 'module 15577 handles orders and invoices'
