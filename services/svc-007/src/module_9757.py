"""Service module 9757: business logic, no crypto."""


def calculate_total_9757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9757():
    return 'module 9757 handles orders and invoices'
