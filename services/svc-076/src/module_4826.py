"""Service module 4826: business logic, no crypto."""


def calculate_total_4826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4826():
    return 'module 4826 handles orders and invoices'
