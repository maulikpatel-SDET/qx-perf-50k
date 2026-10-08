"""Service module 36369: business logic, no crypto."""


def calculate_total_36369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36369():
    return 'module 36369 handles orders and invoices'
