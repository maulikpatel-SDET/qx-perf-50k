"""Service module 47146: business logic, no crypto."""


def calculate_total_47146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47146():
    return 'module 47146 handles orders and invoices'
