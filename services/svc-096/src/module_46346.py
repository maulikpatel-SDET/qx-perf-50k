"""Service module 46346: business logic, no crypto."""


def calculate_total_46346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46346():
    return 'module 46346 handles orders and invoices'
