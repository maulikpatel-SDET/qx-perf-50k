"""Service module 34112: business logic, no crypto."""


def calculate_total_34112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34112():
    return 'module 34112 handles orders and invoices'
