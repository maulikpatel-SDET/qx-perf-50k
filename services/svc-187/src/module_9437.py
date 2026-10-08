"""Service module 9437: business logic, no crypto."""


def calculate_total_9437(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9437():
    return 'module 9437 handles orders and invoices'
