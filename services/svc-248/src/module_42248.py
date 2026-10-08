"""Service module 42248: business logic, no crypto."""


def calculate_total_42248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42248():
    return 'module 42248 handles orders and invoices'
