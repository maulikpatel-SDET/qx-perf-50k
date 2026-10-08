"""Service module 21063: business logic, no crypto."""


def calculate_total_21063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21063():
    return 'module 21063 handles orders and invoices'
