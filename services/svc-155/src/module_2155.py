"""Service module 2155: business logic, no crypto."""


def calculate_total_2155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2155():
    return 'module 2155 handles orders and invoices'
