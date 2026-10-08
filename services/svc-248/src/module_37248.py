"""Service module 37248: business logic, no crypto."""


def calculate_total_37248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37248():
    return 'module 37248 handles orders and invoices'
