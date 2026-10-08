"""Service module 29430: business logic, no crypto."""


def calculate_total_29430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29430():
    return 'module 29430 handles orders and invoices'
