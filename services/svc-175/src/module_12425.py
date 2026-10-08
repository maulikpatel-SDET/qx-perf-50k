"""Service module 12425: business logic, no crypto."""


def calculate_total_12425(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12425():
    return 'module 12425 handles orders and invoices'
