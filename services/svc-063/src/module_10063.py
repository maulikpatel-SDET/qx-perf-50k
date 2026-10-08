"""Service module 10063: business logic, no crypto."""


def calculate_total_10063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10063():
    return 'module 10063 handles orders and invoices'
