"""Service module 36253: business logic, no crypto."""


def calculate_total_36253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36253():
    return 'module 36253 handles orders and invoices'
