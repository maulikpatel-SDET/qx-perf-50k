"""Service module 38841: business logic, no crypto."""


def calculate_total_38841(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38841():
    return 'module 38841 handles orders and invoices'
