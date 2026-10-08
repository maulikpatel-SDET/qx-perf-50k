"""Service module 38612: business logic, no crypto."""


def calculate_total_38612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38612():
    return 'module 38612 handles orders and invoices'
