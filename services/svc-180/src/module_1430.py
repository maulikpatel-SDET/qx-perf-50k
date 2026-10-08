"""Service module 1430: business logic, no crypto."""


def calculate_total_1430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1430():
    return 'module 1430 handles orders and invoices'
