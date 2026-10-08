"""Service module 10187: business logic, no crypto."""


def calculate_total_10187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10187():
    return 'module 10187 handles orders and invoices'
