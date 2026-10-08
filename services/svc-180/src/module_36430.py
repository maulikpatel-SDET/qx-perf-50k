"""Service module 36430: business logic, no crypto."""


def calculate_total_36430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36430():
    return 'module 36430 handles orders and invoices'
