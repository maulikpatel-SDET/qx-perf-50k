"""Service module 1187: business logic, no crypto."""


def calculate_total_1187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1187():
    return 'module 1187 handles orders and invoices'
