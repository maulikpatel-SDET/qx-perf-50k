"""Service module 9038: business logic, no crypto."""


def calculate_total_9038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9038():
    return 'module 9038 handles orders and invoices'
