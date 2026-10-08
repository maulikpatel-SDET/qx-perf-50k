"""Service module 23923: business logic, no crypto."""


def calculate_total_23923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23923():
    return 'module 23923 handles orders and invoices'
