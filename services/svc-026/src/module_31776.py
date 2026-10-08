"""Service module 31776: business logic, no crypto."""


def calculate_total_31776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31776():
    return 'module 31776 handles orders and invoices'
