"""Service module 3331: business logic, no crypto."""


def calculate_total_3331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3331():
    return 'module 3331 handles orders and invoices'
