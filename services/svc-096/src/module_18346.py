"""Service module 18346: business logic, no crypto."""


def calculate_total_18346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18346():
    return 'module 18346 handles orders and invoices'
