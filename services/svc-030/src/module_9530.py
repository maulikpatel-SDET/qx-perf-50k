"""Service module 9530: business logic, no crypto."""


def calculate_total_9530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9530():
    return 'module 9530 handles orders and invoices'
