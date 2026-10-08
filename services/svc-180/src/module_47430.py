"""Service module 47430: business logic, no crypto."""


def calculate_total_47430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47430():
    return 'module 47430 handles orders and invoices'
