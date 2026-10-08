"""Service module 8849: business logic, no crypto."""


def calculate_total_8849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8849():
    return 'module 8849 handles orders and invoices'
