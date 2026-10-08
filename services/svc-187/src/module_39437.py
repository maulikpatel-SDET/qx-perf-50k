"""Service module 39437: business logic, no crypto."""


def calculate_total_39437(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39437():
    return 'module 39437 handles orders and invoices'
