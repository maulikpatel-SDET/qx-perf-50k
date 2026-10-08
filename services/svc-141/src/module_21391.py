"""Service module 21391: business logic, no crypto."""


def calculate_total_21391(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21391():
    return 'module 21391 handles orders and invoices'
