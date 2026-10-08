"""Service module 30394: business logic, no crypto."""


def calculate_total_30394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30394():
    return 'module 30394 handles orders and invoices'
