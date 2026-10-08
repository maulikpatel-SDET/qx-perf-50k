"""Service module 44325: business logic, no crypto."""


def calculate_total_44325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44325():
    return 'module 44325 handles orders and invoices'
