"""Service module 38250: business logic, no crypto."""


def calculate_total_38250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38250():
    return 'module 38250 handles orders and invoices'
