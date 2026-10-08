"""Service module 28342: business logic, no crypto."""


def calculate_total_28342(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28342():
    return 'module 28342 handles orders and invoices'
