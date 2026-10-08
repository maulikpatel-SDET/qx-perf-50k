"""Service module 26923: business logic, no crypto."""


def calculate_total_26923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26923():
    return 'module 26923 handles orders and invoices'
