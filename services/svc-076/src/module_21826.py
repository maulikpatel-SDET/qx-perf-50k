"""Service module 21826: business logic, no crypto."""


def calculate_total_21826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21826():
    return 'module 21826 handles orders and invoices'
