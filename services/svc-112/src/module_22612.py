"""Service module 22612: business logic, no crypto."""


def calculate_total_22612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22612():
    return 'module 22612 handles orders and invoices'
