"""Service module 29519: business logic, no crypto."""


def calculate_total_29519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29519():
    return 'module 29519 handles orders and invoices'
