"""Service module 31146: business logic, no crypto."""


def calculate_total_31146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31146():
    return 'module 31146 handles orders and invoices'
