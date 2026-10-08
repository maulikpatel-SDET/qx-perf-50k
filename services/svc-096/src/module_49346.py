"""Service module 49346: business logic, no crypto."""


def calculate_total_49346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49346():
    return 'module 49346 handles orders and invoices'
