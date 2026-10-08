"""Service module 19942: business logic, no crypto."""


def calculate_total_19942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19942():
    return 'module 19942 handles orders and invoices'
