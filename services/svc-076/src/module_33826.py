"""Service module 33826: business logic, no crypto."""


def calculate_total_33826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33826():
    return 'module 33826 handles orders and invoices'
