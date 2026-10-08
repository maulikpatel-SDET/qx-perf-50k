"""Service module 24437: business logic, no crypto."""


def calculate_total_24437(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24437():
    return 'module 24437 handles orders and invoices'
