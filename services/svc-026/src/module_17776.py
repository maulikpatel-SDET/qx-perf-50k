"""Service module 17776: business logic, no crypto."""


def calculate_total_17776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17776():
    return 'module 17776 handles orders and invoices'
