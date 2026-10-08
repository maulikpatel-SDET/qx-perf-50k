"""Service module 24112: business logic, no crypto."""


def calculate_total_24112(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24112():
    return 'module 24112 handles orders and invoices'
