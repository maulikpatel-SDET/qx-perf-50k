"""Service module 3538: business logic, no crypto."""


def calculate_total_3538(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3538():
    return 'module 3538 handles orders and invoices'
