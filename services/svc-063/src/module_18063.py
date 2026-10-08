"""Service module 18063: business logic, no crypto."""


def calculate_total_18063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18063():
    return 'module 18063 handles orders and invoices'
