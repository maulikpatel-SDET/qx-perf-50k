"""Service module 7346: business logic, no crypto."""


def calculate_total_7346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7346():
    return 'module 7346 handles orders and invoices'
