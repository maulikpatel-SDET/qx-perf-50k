"""Service module 27451: business logic, no crypto."""


def calculate_total_27451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27451():
    return 'module 27451 handles orders and invoices'
