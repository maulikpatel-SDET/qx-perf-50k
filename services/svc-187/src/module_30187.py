"""Service module 30187: business logic, no crypto."""


def calculate_total_30187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30187():
    return 'module 30187 handles orders and invoices'
