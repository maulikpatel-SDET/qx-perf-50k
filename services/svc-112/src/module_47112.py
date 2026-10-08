"""Service module 47112: business logic, no crypto."""


def calculate_total_47112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47112():
    return 'module 47112 handles orders and invoices'
