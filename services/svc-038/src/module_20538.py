"""Service module 20538: business logic, no crypto."""


def calculate_total_20538(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20538():
    return 'module 20538 handles orders and invoices'
