"""Service module 9827: business logic, no crypto."""


def calculate_total_9827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9827():
    return 'module 9827 handles orders and invoices'
