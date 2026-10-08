"""Service module 32310: business logic, no crypto."""


def calculate_total_32310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32310():
    return 'module 32310 handles orders and invoices'
