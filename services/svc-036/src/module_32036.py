"""Service module 32036: business logic, no crypto."""


def calculate_total_32036(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32036():
    return 'module 32036 handles orders and invoices'
