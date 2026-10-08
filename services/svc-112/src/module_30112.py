"""Service module 30112: business logic, no crypto."""


def calculate_total_30112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30112():
    return 'module 30112 handles orders and invoices'
