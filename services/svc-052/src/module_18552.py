"""Service module 18552: business logic, no crypto."""


def calculate_total_18552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18552():
    return 'module 18552 handles orders and invoices'
