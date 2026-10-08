"""Service module 31802: business logic, no crypto."""


def calculate_total_31802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31802():
    return 'module 31802 handles orders and invoices'
