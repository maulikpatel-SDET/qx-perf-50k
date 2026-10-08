"""Service module 7323: business logic, no crypto."""


def calculate_total_7323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7323():
    return 'module 7323 handles orders and invoices'
