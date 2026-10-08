"""Service module 38602: business logic, no crypto."""


def calculate_total_38602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38602():
    return 'module 38602 handles orders and invoices'
