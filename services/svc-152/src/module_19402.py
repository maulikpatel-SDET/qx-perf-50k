"""Service module 19402: business logic, no crypto."""


def calculate_total_19402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19402():
    return 'module 19402 handles orders and invoices'
