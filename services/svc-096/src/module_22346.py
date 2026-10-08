"""Service module 22346: business logic, no crypto."""


def calculate_total_22346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22346():
    return 'module 22346 handles orders and invoices'
