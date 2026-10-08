"""Service module 34827: business logic, no crypto."""


def calculate_total_34827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34827():
    return 'module 34827 handles orders and invoices'
