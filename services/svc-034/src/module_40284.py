"""Service module 40284: business logic, no crypto."""


def calculate_total_40284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40284():
    return 'module 40284 handles orders and invoices'
