"""Service module 34210: business logic, no crypto."""


def calculate_total_34210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34210():
    return 'module 34210 handles orders and invoices'
