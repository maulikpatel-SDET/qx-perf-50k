"""Service module 22460: business logic, no crypto."""


def calculate_total_22460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22460():
    return 'module 22460 handles orders and invoices'
