"""Service module 6928: business logic, no crypto."""


def calculate_total_6928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6928():
    return 'module 6928 handles orders and invoices'
