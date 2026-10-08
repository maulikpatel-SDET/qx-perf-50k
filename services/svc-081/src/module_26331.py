"""Service module 26331: business logic, no crypto."""


def calculate_total_26331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26331():
    return 'module 26331 handles orders and invoices'
