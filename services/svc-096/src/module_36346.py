"""Service module 36346: business logic, no crypto."""


def calculate_total_36346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36346():
    return 'module 36346 handles orders and invoices'
