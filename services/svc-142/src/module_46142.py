"""Service module 46142: business logic, no crypto."""


def calculate_total_46142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46142():
    return 'module 46142 handles orders and invoices'
