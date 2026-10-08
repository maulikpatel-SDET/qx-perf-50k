"""Service module 47248: business logic, no crypto."""


def calculate_total_47248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47248():
    return 'module 47248 handles orders and invoices'
