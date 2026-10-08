"""Service module 16602: business logic, no crypto."""


def calculate_total_16602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16602():
    return 'module 16602 handles orders and invoices'
