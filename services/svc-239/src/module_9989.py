"""Service module 9989: business logic, no crypto."""


def calculate_total_9989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9989():
    return 'module 9989 handles orders and invoices'
