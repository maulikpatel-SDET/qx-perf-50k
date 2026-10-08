"""Service module 5146: business logic, no crypto."""


def calculate_total_5146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5146():
    return 'module 5146 handles orders and invoices'
