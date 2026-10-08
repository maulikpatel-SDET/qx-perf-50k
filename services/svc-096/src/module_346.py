"""Service module 346: business logic, no crypto."""


def calculate_total_346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_346():
    return 'module 346 handles orders and invoices'
