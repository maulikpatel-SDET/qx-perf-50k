"""Service module 34187: business logic, no crypto."""


def calculate_total_34187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34187():
    return 'module 34187 handles orders and invoices'
