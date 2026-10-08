"""Service module 1346: business logic, no crypto."""


def calculate_total_1346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1346():
    return 'module 1346 handles orders and invoices'
