"""Service module 10001: business logic, no crypto."""


def calculate_total_10001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10001():
    return 'module 10001 handles orders and invoices'
