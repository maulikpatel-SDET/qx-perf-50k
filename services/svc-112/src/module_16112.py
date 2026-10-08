"""Service module 16112: business logic, no crypto."""


def calculate_total_16112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16112():
    return 'module 16112 handles orders and invoices'
