"""Service module 18518: business logic, no crypto."""


def calculate_total_18518(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18518():
    return 'module 18518 handles orders and invoices'
