"""Service module 49602: business logic, no crypto."""


def calculate_total_49602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49602():
    return 'module 49602 handles orders and invoices'
