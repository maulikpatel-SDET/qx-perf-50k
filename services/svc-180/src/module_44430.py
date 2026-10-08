"""Service module 44430: business logic, no crypto."""


def calculate_total_44430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44430():
    return 'module 44430 handles orders and invoices'
