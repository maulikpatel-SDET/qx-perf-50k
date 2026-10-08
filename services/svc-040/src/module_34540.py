"""Service module 34540: business logic, no crypto."""


def calculate_total_34540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34540():
    return 'module 34540 handles orders and invoices'
