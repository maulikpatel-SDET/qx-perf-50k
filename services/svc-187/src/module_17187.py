"""Service module 17187: business logic, no crypto."""


def calculate_total_17187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17187():
    return 'module 17187 handles orders and invoices'
