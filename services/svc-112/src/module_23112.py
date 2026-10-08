"""Service module 23112: business logic, no crypto."""


def calculate_total_23112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23112():
    return 'module 23112 handles orders and invoices'
