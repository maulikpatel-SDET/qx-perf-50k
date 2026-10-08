"""Service module 27059: business logic, no crypto."""


def calculate_total_27059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27059():
    return 'module 27059 handles orders and invoices'
