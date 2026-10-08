"""Service module 39112: business logic, no crypto."""


def calculate_total_39112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39112():
    return 'module 39112 handles orders and invoices'
