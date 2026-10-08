"""Service module 40428: business logic, no crypto."""


def calculate_total_40428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40428():
    return 'module 40428 handles orders and invoices'
