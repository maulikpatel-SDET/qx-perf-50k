"""Service module 15314: business logic, no crypto."""


def calculate_total_15314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15314():
    return 'module 15314 handles orders and invoices'
