"""Service module 42346: business logic, no crypto."""


def calculate_total_42346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42346():
    return 'module 42346 handles orders and invoices'
