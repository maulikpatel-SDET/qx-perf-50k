"""Service module 40187: business logic, no crypto."""


def calculate_total_40187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40187():
    return 'module 40187 handles orders and invoices'
