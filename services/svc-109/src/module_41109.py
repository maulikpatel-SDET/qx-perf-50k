"""Service module 41109: business logic, no crypto."""


def calculate_total_41109(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41109():
    return 'module 41109 handles orders and invoices'
