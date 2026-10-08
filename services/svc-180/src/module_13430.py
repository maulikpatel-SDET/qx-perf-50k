"""Service module 13430: business logic, no crypto."""


def calculate_total_13430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13430():
    return 'module 13430 handles orders and invoices'
