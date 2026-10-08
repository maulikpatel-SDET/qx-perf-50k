"""Service module 16513: business logic, no crypto."""


def calculate_total_16513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16513():
    return 'module 16513 handles orders and invoices'
