"""Service module 25540: business logic, no crypto."""


def calculate_total_25540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25540():
    return 'module 25540 handles orders and invoices'
