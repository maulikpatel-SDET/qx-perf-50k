"""Service module 15049: business logic, no crypto."""


def calculate_total_15049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15049():
    return 'module 15049 handles orders and invoices'
