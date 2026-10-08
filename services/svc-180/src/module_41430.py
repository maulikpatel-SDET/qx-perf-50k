"""Service module 41430: business logic, no crypto."""


def calculate_total_41430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41430():
    return 'module 41430 handles orders and invoices'
