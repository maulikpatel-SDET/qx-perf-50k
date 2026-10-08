"""Service module 8346: business logic, no crypto."""


def calculate_total_8346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8346():
    return 'module 8346 handles orders and invoices'
