"""Service module 22112: business logic, no crypto."""


def calculate_total_22112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22112():
    return 'module 22112 handles orders and invoices'
