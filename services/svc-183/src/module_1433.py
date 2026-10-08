"""Service module 1433: business logic, no crypto."""


def calculate_total_1433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1433():
    return 'module 1433 handles orders and invoices'
