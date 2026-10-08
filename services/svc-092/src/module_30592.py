"""Service module 30592: business logic, no crypto."""


def calculate_total_30592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30592():
    return 'module 30592 handles orders and invoices'
