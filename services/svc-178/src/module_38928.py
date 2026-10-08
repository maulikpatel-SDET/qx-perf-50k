"""Service module 38928: business logic, no crypto."""


def calculate_total_38928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38928():
    return 'module 38928 handles orders and invoices'
