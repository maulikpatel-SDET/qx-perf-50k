"""Service module 21112: business logic, no crypto."""


def calculate_total_21112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21112():
    return 'module 21112 handles orders and invoices'
