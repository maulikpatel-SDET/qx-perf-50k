"""Service module 10346: business logic, no crypto."""


def calculate_total_10346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10346():
    return 'module 10346 handles orders and invoices'
