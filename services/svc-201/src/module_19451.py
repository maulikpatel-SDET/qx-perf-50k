"""Service module 19451: business logic, no crypto."""


def calculate_total_19451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19451():
    return 'module 19451 handles orders and invoices'
